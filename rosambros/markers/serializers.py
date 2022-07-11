from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField
from .models import Marker
import re
# from rosambros.settings import model
from PIL import Image
import numpy as np

# def validate_single(_img):
#     # img = keras_image.load_img(img_path, target_size=(200,200))
#     # x = keras_image.img_to_array(img)
#     img = Image.open(_img)
#     img.resize((200,200))
#     x = np.array(img)
#     x = np.expand_dims(x, axis=0)
#     images = np.vstack([x])
#     classes = model.predict(images, batch_size=10)
#     result = False
#     if classes[0] < 0.5:
#         # Ambrosia
#         print('Ambrosia')
#         result = True
#     else:
#         # Not ambrosia
#         print('Not ambrosia')
#         result = False
#     return result

class MarkerExportSerializer(serializers.ModelSerializer):
  class Meta:
    model = Marker
    fields = (
      'street',
      'gps',
      'created_on',
      'description',
    )

class MarkerSerializer(serializers.ModelSerializer):
  image = Base64ImageField()
  class Meta:
    model = Marker
    fields = (
      'id',
      'street',
      'name',
      'description',
      'marker_type',
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
    marker_type = validated_data.pop('marker_type')

    pattern = '^[-+]?([1-8]?\d(\.\d+)?|90(\.0+)?),\s*[-+]?(180(\.0+)?|((1[0-7]\d)|([1-9]?\d))(\.\d+)?)$'
    match_result = re.match(pattern, gps)

    if match_result:
      print('OK')
    else:
      error = { 'message': 'Validation error. Your data: {} is invalid.'.format(gps) }
      raise serializers.ValidationError(error)
    
    # if marker_type == 1: # if ambros
    #   try:
    #     val_res = validate_single(image.image)
    #     if val_res:
    #       pass
    #     else:
    #       error = { 'message': 'Validation error. Image is not ambrosia. Denied' }
    #       raise serializers.ValidationError(error)
    #   except Exception as e:
    #     print(e)

    # if not ambros, STOP IMMEDIATE
    # if marker_type != 1:
    #   error = { 'message': 'Validation error. You need send marker_type=1, only ambros, not road.' }
    #   raise serializers.ValidationError(error)
    
    # Нейросеть для премодерации абмрозии.....
    # try:
    #   val_res = validate_single(image.image)
    #   if val_res:
    #     pass
    #   else:
    #     error = { 'message': 'Validation error. Image is not ambrosia. Accepted, but denied.' }
    #     raise serializers.ValidationError(error)
    # except Exception as e:
    #   print(e)

    try:
      name = validated_data.pop('name')
    except Exception as e:
      pass

    try:
      description = validated_data.pop('description')
    except Exception as e:
      pass
    
    try:
      marker = Marker.objects.create(name=name, description=description, gps=gps, image=image, marker_type=marker_type)
      return marker
    except Exception as e:
      error = {'message': ",".join(e.args) if len(e.args) > 0 else 'Unknown Error'}
      raise serializers.ValidationError(error)