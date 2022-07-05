from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import MarkerImageBase64, MarkerList, MarkerDetail, MarkerUpload, MarkerDelete, MarkerExportCSV, MarkerExportJson

urlpatterns = [
  path('markers/', MarkerList.as_view(), name='markers'),
  path('markers/upload/', MarkerUpload.as_view(), name='markers_upload'),
  path('markers/<int:pk>/', MarkerDetail.as_view(), name='marker_detail'),
  path('markers/<int:pk>/get_image_base64/', MarkerImageBase64.as_view(), name='marker_image_base64'),
  path('markers/delete/<int:pk>', MarkerDelete.as_view(), name='marker_delete'),
  path('markers/export_csv', MarkerExportCSV.as_view(), name='marker_export_csv'),
  path('markers/export_markers_json', MarkerExportJson.as_view(), name='export_markers_json')
]