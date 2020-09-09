from django.db import models

from django.contrib.gis.db import models

from django_countries.fields import CountryField

from phone_field import PhoneField

# Create your models here.

#Datos de las organizaciones
class Organizacion(models.Model):
	id = models.AutoField(primary_key = True)
	nombre = models.CharField(max_length = 200, blank = False, null = False)
	telefono_organizacion = PhoneField(blank=True, help_text='su numero de contacto')
	observacion = models.TextField(blank = False, null = False)

	class Meta:
		verbose_name = 'Organizacion'
		verbose_name_plural = 'Organizaciones'
		ordering = ['nombre']

	def __str__(self):
		return '%s %s %s' % (self.nombre, self.contacto, self.observacion)

#Datos de las Personas
class Persona(models.Model):

	nombre = models.CharField(max_length = 50, blank = False, null = False)
	apellido = models.CharField(max_length = 50, blank = False, null = False)
	ci_nro = models.CharField(max_length = 8, blank = False, null = False, primary_key = True)
	telefono_persona = PhoneField(blank=True, help_text='su numero de contacto')
	pais = CountryField()
	fecha_nacimiento = models.DateField()
	ubicacion = models.PointField()
	direccion = models.CharField(max_length = 100, blank = False, null = False)
	observacion = models.TextField(blank = False, null = False)
	organizacion = models.ForeignKey(Organizacion, on_delete = models.CASCADE)


	class Meta:
		verbose_name = 'Persona'
		verbose_name_plural = 'Personas'
		ordering = ['ci_nro']

	def __str__(self):
		return '%s %s %s' % (self.ci_nro, self.nombre, self.apellido)