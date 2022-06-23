from django.db import models
from django.dispatch import receiver
import os
from PIL import Image
from rosambros.settings import DOMAIN_PORT
from django.core.files import File
from io import BytesIO
from django.core.files.base import ContentFile
from PIL import Image
import numpy as np
from rosambros.settings import model
import logging

STATUS = (
  (0, "Draft"),
  (1, "Publish"),
)

MARKER_TYPE = (
  (0, "road"),
  (1, "ambros"),
)

logger = logging.getLogger(__name__)

class Marker(models.Model):
  name = models.CharField(max_length=200, blank=True, null=True)
  description = models.TextField(blank=True, null=True)
  marker_type = models.IntegerField(choices=MARKER_TYPE, default=0)
  gps = models.CharField(max_length=200)
  image = models.ImageField(upload_to='uploads/',  blank=True, null=True)
  thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
  created_on = models.DateTimeField(auto_now_add=True)

  class Meta:
    ordering = ('-created_on',)
  
  def __str__(self):
    return f'{self.id}_{self.name}'
  
  def save(self, *args, **kwargs):
    if self.image:
      filename = '{}.jpg'.format(self.image.name.split('.')[0].lstrip('uploads/'))

      image = Image.open(self.image)
      # For PNG images discarding the alpha channel and fill it with some color
      if image.mode in ('RGBA', 'LA'):
        background = Image.new(image.mode[:-1], image.size, '#fff')
        background.paste(image, image.split()[-1])
        image = background
      image_io = BytesIO()
      image.save(image_io, format='JPEG', quality=100)

      # change the image field value to be the newly modified image value
      self.image.save(filename, ContentFile(image_io.getvalue()), save=False)
    
    try:
      print('Before validation')
      logger.info('before validation')
      # print(self.image.image)
      print(dir(self.image))
      val_res = self.validate_single(self.image)
      print('After validation')
      logger.info('After validation')
      if val_res:
        print('Before save')
        logger.info('Before save')
        super(Marker, self).save(*args, **kwargs)
    except Exception as e:
      print("EXCEPTION" + str(e))
  
  def get_image(self):
    if self.image:
      return DOMAIN_PORT + self.image.url
    return ''

  def get_thumbnail(self):
    serv_url = DOMAIN_PORT
    if self.thumbnail:
      return serv_url + self.thumbnail.url
    else:
      if self.image:
        self.thumbnail = self.make_thumbnail(self.image)
        self.save()

        return serv_url + self.thumbnail.url
      else:
        return ''
  
  def make_thumbnail(self, image, size=(300, 300)):
    img = Image.open(image)

    img.convert('RGB')
    img.thumbnail(size)

    thumb_io = BytesIO()
    img.save(thumb_io, 'JPEG', quality=85)

    thumbnail = File(thumb_io, name=image.name)
    
    return thumbnail
  
  def validate_single(self, _img):
    # img = keras_image.load_img(img_path, target_size=(200,200))
    # x = keras_image.img_to_array(img)
    print('Opening image and resizing it')
    img = Image.open(_img)
    print('Image information before resize:', img.size)
    img = img.resize((200,200))
    print('Image information after resize:', img.size)
    print(2222)
    x = np.array(img)
    print(3333)
    x = np.expand_dims(x, axis=0)
    print(4444)
    images = np.vstack([x])
    print(5555)
    classes = model.predict(images, batch_size=10)
    print(6666)
    result = False
    if classes[0] < 0.5:
        # Ambrosia
        print('Ambrosia')
        logger.info('ambrosia')
        result = True
    else:
        # Not ambrosia
        print('Not ambrosia')
        logger.info('not ambrosia')
        result = False
    return result