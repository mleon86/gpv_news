from django.contrib import admin

from django.contrib.gis import admin
from django.contrib.gis.admin import OSMGeoAdmin

# Register your models here.
from .models import Organizacion, Persona

admin.site.register(Organizacion)

@admin.register(Persona)
class PersonaAdmin(OSMGeoAdmin):
	default_lon = -6403019.37589
	default_lat = -2909670.42369
	default_zoom = 13