from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import MarkerList, MarkerDetail, MarkerUpload

urlpatterns = [
  path('markers/', MarkerList.as_view(), name='markers'),
  path('markers/upload/', MarkerUpload.as_view(), name='markers_upload'),
  path('markers/<int:pk>/', MarkerDetail.as_view(), name='marker_detail'),
]