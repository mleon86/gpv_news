from django.contrib.gis.db import models

from ckeditor.fields import RichTextField


# Create your models here.

class Autor (models.Model):
	nombres = models.CharField("Nombres del Autor", max_length=255, null = False, blank = False)
	apellidos = models.CharField("Apellidos del Autor", max_length=255, null = False, blank = False)	
	image = models.URLField("Imagen del Autor", max_length = 255, null = True, blank = True)
	facebook  = models.URLField("Facebook", max_length = 255, null = True, blank = True)
	twiter = models.URLField("Twiter", max_length = 255, null = True, blank = True)
	instagram = models.URLField("Instagram", max_length = 255, null = True, blank = True)
	fecha_creacion = models.DateTimeField("Fecha de Cración", auto_now=True, auto_now_add=False, null=True)
	fecha_actualizacion = models.DateTimeField("Fecha de Actualización", auto_now=False, auto_now_add=True, null=True)

	class Meta:
		verbose_name = 'Author'
		verbose_name_plural = 'Autores'
		ordering = ['nombres']

	def __str__(self):
		return '%s %s %s' % (self.nombres, self.apellidos, self.fecha_creacion)


class Post(models.Model):
	titulo = models.CharField("Titulo del Post", max_length=255, null = False, blank = False)
	body = RichTextField("Contenido del Post", max_length = 1023, null = False, blank = False)
	imagen = models.URLField("Imagen del Post", max_length = 255, null = True, blank = True)
	autor = models.ForeignKey(Autor, on_delete= models.CASCADE, null=True) 
	fecha_creacion = models.DateTimeField("Fecha de Cración", auto_now=True, auto_now_add=False, null=True)
	fecha_actualizacion = models.DateTimeField("Fecha de Actualización", auto_now=False, auto_now_add=True, null=True)

	class Meta:
		verbose_name = 'Post'
		verbose_name_plural = 'Posteos'
		ordering = ['fecha_creacion']

	def __str__(self):
		return '%s %s %s' % (self.titulo, self.fecha_creacion, self.fecha_actualizacion)