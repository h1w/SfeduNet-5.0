from django.contrib import admin
from .models import Marker

class MarkerAdmin(admin.ModelAdmin):
  list_display = ('name', 'description', 'gps', 'created_on',)
  list_filter = ('name', 'created_on',)
  search_filter = ('name', 'description', 'gps', 'created_on',)

admin.site.register(Marker, MarkerAdmin)

admin.site.site_header="Marker"