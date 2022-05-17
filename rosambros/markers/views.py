from django.db.models import Q
from django.http import Http404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Marker
from .serializers import MarkerSerializer

from django.shortcuts import get_object_or_404
import base64
from io import BytesIO
from rosambros.settings import MEDIA_ROOT
from PIL import Image

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
    serializer = MarkerSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
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