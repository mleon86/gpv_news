from django.contrib import admin

from .models import *

from import_export import resources
from import_export.admin import ImportExportModelAdmin

class CategoriaResource(resources.ModelResource):
	class Meta:
		model = Categoria

class CategoriaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
	search_fields = ['nombre']
	list_display = ('nombre', 'fecha_creacion')


class PostResource(resources.ModelResource):
	class Meta:
		model = Post

class PostAdmin(ImportExportModelAdmin, admin.ModelAdmin):
	search_fields = ['titulo']
	list_display = ('fecha_creacion', 'titulo', 'autor')

class AutorResource(resources.ModelResource):
	class Meta:
		model = Autor

class AutorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
	search_fields = ['nombres']
	list_display = ('nombres', 'fecha_creacion')


admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Autor, AutorAdmin)
