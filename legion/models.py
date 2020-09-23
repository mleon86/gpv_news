from django.db import models

from django.contrib.gis.db import models

from django_countries.fields import CountryField

from phone_field import PhoneField

# Create your models here.

#Datos de las organizaciones
class Organizacion(models.Model):
	id = models.AutoField("identificador",primary_key = True)
	nombre = models.CharField("Nombre", max_length = 200, blank = False, null = False)
	telefono_organizacion = models.CharField("Teléfono", max_length = 20, blank=True, help_text='su numero de contacto')
	observacion = models.TextField("Observación",blank = False, null = False)

	class Meta:
		verbose_name = 'Organizacion'
		verbose_name_plural = 'Organizaciones'
		ordering = ['nombre']

	def __str__(self):
		return '%s %s %s' % (self.nombre, self.telefono_organizacion, self.observacion)

#Datos de las Personas
class Persona(models.Model):

	nombre = models.CharField("Nombre",max_length = 50, blank = False, null = False)
	apellido = models.CharField("Apellido", max_length = 50, blank = False, null = False)
	ci_nro = models.CharField("Cedula de identidad", max_length = 8, blank = False, null = False, primary_key = True)
	telefono_persona = models.CharField("Teléfono", max_length = 20, blank=True, help_text='su numero de contacto')
	pais = CountryField()
	fecha_nacimiento = models.DateField()
	ubicacion = models.PointField()
	direccion = models.CharField("Direccion",max_length = 100, blank = False, null = False)
	observacion = models.TextField("Observacion",blank = False, null = False)
	organizacion = models.ForeignKey(Organizacion, blank = True, on_delete = models.CASCADE)


	class Meta:
		verbose_name = 'Persona'
		verbose_name_plural = 'Personas'
		ordering = ['ci_nro']

	def __str__(self):
		return '%s %s %s' % (self.ci_nro, self.nombre, self.apellido)