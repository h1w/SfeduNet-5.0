from django.contrib import admin
from .models import Marker

class MarkerAdmin(admin.ModelAdmin):
  list_display = ('street', 'name', 'description', 'marker_type', 'gps', 'created_on',)
  list_filter = ('marker_type', 'created_on',)
  search_filter = ('street', 'name', 'description', 'gps', 'marker_type', 'created_on',)

admin.site.register(Marker, MarkerAdmin)

admin.site.site_header="Marker"