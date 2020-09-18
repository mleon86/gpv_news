from django.contrib import admin

from .models import *
# Register your models here.

class PostAdmin(admin.ModelAdmin):
	search_fields = ['titulo']
	list_display = ('titulo', 'fecha_creacion')

class AutorAdmin(admin.ModelAdmin):
	search_fields = ['nombre']


admin.site.register(Post, PostAdmin)
admin.site.register(Autor, AutorAdmin)