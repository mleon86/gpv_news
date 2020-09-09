from rest_framework import serializers
from .models import Organizacion, Persona

class OrganizacionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Organizacion
		fields = '__all__'

class PersonaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Persona
		fields = '__all__'