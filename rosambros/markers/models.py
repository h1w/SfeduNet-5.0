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
import requests
import json
import requests

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
  street = models.TextField(blank=True, null=True)

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
      # print(self.image.image)
      print(dir(self.image))
      val_res = self.validate_single(filename)#self.image)
      if val_res:
        # Получить улицу
        response = requests.get(f'''https://nominatim.openstreetmap.org/reverse?lat={self.gps.split(',')[0].strip(' ')}&lon={self.gps.split(',')[1].strip(' ')}&format=json''')
        jsn = json.loads(response.content.decode())
        s = str(jsn['display_name'])
        s = ' ' + s
        s = s.split(',')
        self.street = ','.join(s[::-1])
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
    result = False
    img_dir = "../../media/SfeduNet-5.0/uploads/"+_img
    
    API_KEY = "2b10je0sSNo4jcq5U4Ij21RF"	# Your API_KEY here
    api_endpoint = f"https://my-api.plantnet.org/v2/identify/all?api-key={API_KEY}"
    image_data_1 = open(img_dir, 'rb')

    data = {
        'organs': ['leaf']
    }

    files = [
        ('images', (img_dir, image_data_1))
    ]

    req = requests.Request('POST', url=api_endpoint, files=files, data=data)
    prepared = req.prepare()

    s = requests.Session()
    response = s.send(prepared)
    json_result = json.loads(response.text)

    if response.status_code == 200:
        formatet_json = json.dumps(json_result, indent=3)
        print(formatet_json)

        print(json_result["bestMatch"])
        if "Ambrosia" in json_result["bestMatch"] or "Artemisia" in json_result["bestMatch"]:
            # print("Yeah that's ambrosia: ", json_result["bestMatch"])
            result = True
        else:
            result = False
            # print("Sorry that's not an Ambrosia")
    else:
        result = False
        # print("Sorry that's not an Ambrosia")
    print(response.status_code)
    print(result)
    return result
    # # img = keras_image.load_img(img_path, target_size=(200,200))
    # # x = keras_image.img_to_array(img)
    # # print('Opening image and resizing it')
    # img = Image.open(_img)
    # # print('Image information before resize:', img.size)
    # img = img.resize((200,200))
    # # print('Image information after resize:', img.size)
    # x = np.array(img)
    # x = np.expand_dims(x, axis=0)
    # images = np.vstack([x])
    # classes = model.predict(images, batch_size=10)
    # result = False
    # if classes[0] < 0.5:
    #     # Ambrosia
    #     print('Ambrosia')
    #     logger.info('ambrosia')
    #     result = True
    # else:
    #     # Not ambrosia
    #     print('Not ambrosia')
    #     logger.info('not ambrosia')
    #     result = False
    # return True
