from django.db import models

from django.contrib.gis.db import models

from django_countries.fields import CountryField

from phone_field import PhoneField

from ckeditor.fields import RichTextField

# Create your models here.


#Datos de las organizaciones

class Leccion(models.Model):
	title = models.CharField(max_length=150)
	body = RichTextField()
	image = models.ImageField(upload_to="post_image", null=True)
	video_leccion = models.CharField(max_length = 150)
	create_at = models.DateTimeField(auto_now=True, auto_now_add=False, null=True)
	update_at = models.DateTimeField(auto_now=False, auto_now_add=True, null=True)

	
	class Meta:
		verbose_name = 'Leccion'
		verbose_name_plural = 'Lecciones'
		ordering = ['create_at']

	def __str__(self):
		return '%s %s %s' % (self.title, self.create_at, self.update_at)

class Curso(models.Model):
	title = models.CharField(max_length = 150)
	comentario = models.CharField(max_length = 200)
	video_invitacion = models.CharField(max_length = 150)
	create_at = models.DateTimeField(auto_now=True, auto_now_add=False, null=True)
	update_at = models.DateTimeField(auto_now=False, auto_now_add=True, null=True)
	lecciones = models.ManyToManyField(Leccion)

	class Meta:
		verbose_name = 'Curso'
		verbose_name_plural = 'Cursos'
		ordering = ['create_at']

	def __str__(self):
		return '%s %s %s' % (self.title, self.create_at, self.update_at)

# Create your models here.
