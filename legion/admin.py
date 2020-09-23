from django.contrib import admin

from django.contrib.gis import admin
from django.contrib.gis.admin import OSMGeoAdmin

from import_export import resources
from import_export.admin import ImportExportModelAdmin


# Register your models here.
from .models import Organizacion, Persona

class OrganizacionResource(resources.ModelResource):
	class Meta:
		model = Organizacion


class OrganizacionAdmin(ImportExportModelAdmin, OSMGeoAdmin):
	search_fields = ['nombre']
	list_display = ('nombre', 'telefono_organizacion', 'observacion')


class PersonaResource(resources.ModelResource):
	class Meta:
		model = Persona

class PersonaAdmin(ImportExportModelAdmin, OSMGeoAdmin):
	search_fields = ['nombre']
	list_display = ('nombre', 'apellido', 'fecha_nacimiento')
	resource_class = PersonaResource
	default_lon = -6403019.37589
	default_lat = -2909670.42369
	default_zoom = 13


admin.site.register(Organizacion, OrganizacionAdmin)
admin.site.register(Persona, PersonaAdmin)