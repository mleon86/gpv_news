from rest_framework import serializers
from .models import Curso, Leccion

class CursoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Curso
		fields = '__all__'

class LeccionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Leccion
		fields = '__all__'