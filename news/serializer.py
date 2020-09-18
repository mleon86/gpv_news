from rest_framework import serializers
from .models import *

class PostSerializer(serializers.ModelSerializer):
	class Meta:
		model = Post
		fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Autor
		fields = '__all__'