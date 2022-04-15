from django.db import models
from django.dispatch import receiver
import os
from PIL import Image
from rosambros.settings import DOMAIN_PORT
from django.core.files import File
from io import BytesIO

STATUS = (
  (0, "Draft"),
  (1, "Publish"),
)

class Marker(models.Model):
  name = models.CharField(max_length=200, blank=True, null=True)
  description = models.TextField(blank=True, null=True)
  gps = models.CharField(max_length=200)
  image = models.ImageField(upload_to='uploads/',  blank=True, null=True)
  thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
  created_on = models.DateTimeField(auto_now_add=True)

  class Meta:
    ordering = ('-created_on',)
  
  def __str__(self):
    return f'{self.id}_{self.name}'
  
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