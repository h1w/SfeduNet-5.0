from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField
from .models import Marker

class MarkerSerializer(serializers.ModelSerializer):
  image = Base64ImageField()
  class Meta:
    model = Marker
    fields = (
      'id',
      'name',
      'description',
      'gps',
      'image',
      'get_image',
      'get_thumbnail',
      'created_on',
    )
  def create(self, validated_data):
    name = 'None'
    description = ''
    image = validated_data.pop('image')
    gps = validated_data.pop('gps')
    
    try:
      name = validated_data.pop('name')
    except Exception as e:
      pass

    try:
      description = validated_data.pop('description')
    except Exception as e:
      pass

    return Marker.objects.create(name=name, description=description, gps=gps, image=image)