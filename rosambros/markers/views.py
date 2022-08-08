from django.db.models import Q
from django.http import Http404, JsonResponse, HttpResponse, HttpResponseNotFound

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated

from .models import Marker
from .serializers import MarkerSerializer, MarkerExportSerializer

from django.shortcuts import get_object_or_404
import base64
from io import BytesIO
from rosambros.settings import MEDIA_ROOT, REPOSITORY_DIR, DAILY_UPLOAD_FILE_ABSPATH
from PIL import Image
import requests
import json
import csv
from datetime import datetime
import os

class MarkerList(APIView):
  def get(self, request, format=None):
    markers = Marker.objects.all()
    serializer = MarkerSerializer(markers, many=True)
    return Response(serializer.data)

class MarkerDetail(APIView):
  def get(self, request, pk, format=None):
    marker = Marker.objects.get(id=pk)
    serializer = MarkerSerializer(marker)
    return Response(serializer.data)

class MarkerUpload(APIView):
  def post(self, request, format=None):
    print("Pushed into serializer")
    serializer = MarkerSerializer(data=request.data)
    if serializer.is_valid():
      print("Serislizing")
      serializer.save()
      print("Saved after serializer")
      return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MarkerImageBase64(APIView):
  def get(self, request, pk, format=None):
    marker = get_object_or_404(Marker, id=pk)
    img_path = (str(MEDIA_ROOT) + marker.image.url.lstrip('/media/'))
    img = Image.open(img_path)
    buffered = BytesIO()
    img.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue())

    context = {
      'image_base64': img_str,
    }

    return Response(context, status=status.HTTP_200_OK)

class MarkerDelete(APIView):
  permission_classes = [IsAuthenticated]
  def delete(self, request, pk, format=None):
    marker = Marker.objects.get(id=pk)
    marker.delete()
    return Response({"message": "Marker with id `{}` has been deleted.".format(pk)}, status=status.HTTP_200_OK)

class MarkerExportCSV(APIView):
  permission_classes = [IsAuthenticated]
  def get(self, request, format=None):
    daily_upload_abspath = DAILY_UPLOAD_FILE_ABSPATH

    with open(daily_upload_abspath, 'r') as f:
      file_data = f.read()

    # sending response 
    response = HttpResponse(file_data, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="DailyUpload.csv"'

    return response


# class MarkerExportCSV(APIView):
#   def get(self, request, format=None):
#     markers = Marker.objects.all()
#     m_e = []
#     for marker in markers:
#       resposne = requests.get(f'''https://nominatim.openstreetmap.org/reverse?lat={marker.gps.split(',')[0].strip(' ')}&lon={marker.gps.split(',')[1].strip(' ')}&format=json''')
#       jsn = json.loads(resposne.content.decode())
#       street = ''
#       street += str(jsn['address']['road'])
#       if 'house_number' in jsn['address']:
#         street += ' ' + str(jsn['address']['house_number'])
#       dt_object = datetime.fromtimestamp(marker.created_on.timestamp())
#       createdon = dt_object.strftime("%d.%m.%Y %H:%M:%S")
#       marker_obj = {
#         'street': street,
#         'gps': marker.gps,
#         'created_on': createdon
#       }
#       m_e.append(marker_obj)
    
#     response = HttpResponse(
#       content_type='text/csv',
#       headers={
#         'Content-Disposition': 'attachment; filename="DailyUpload.csv"'
#       },
#     )
#     response.write(u'\ufeff'.encode('utf8'))

#     header = ['Координаты', 'Улица', 'Дата и время']
#     writer = csv.writer(response, delimiter=';')
#     writer.writerow(header)

#     for marker in m_e:
#       writer.writerow([marker['gps'], marker['street'], marker['created_on']])

#     return response

class MarkerExportJson(APIView):
  def get(self, request, format=None):
    markers = Marker.objects.all()
    serializer = MarkerExportSerializer(markers, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)