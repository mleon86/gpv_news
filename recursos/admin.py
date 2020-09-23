from django.contrib import admin

from .models import Curso, Leccion

from import_export import resources
from import_export.admin import ImportExportModelAdmin

class CursoResource(resources.ModelResource):
	class Meta:
		model = Curso

class CursoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
	search_fields = ['titulo']
	list_display = ('titulo', 'create_at')

class LeccionResource(resources.ModelResource):
	class Meta:
		model = Leccion

class LeccionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
	search_fields = ['titulo']
	list_display = ('titulo', 'create_at')


admin.site.register(Curso, CursoAdmin)
admin.site.register(Leccion, LeccionAdmin)