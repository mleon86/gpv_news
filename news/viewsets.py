from rest_framework import viewsets

from .models import *
from .serializer import PostSerializer, AuthorSerializer


class PostViewSet(viewsets.ModelViewSet):
	queryset = Post.objects.all()
	serializer_class = PostSerializer

class AuthorViewSet(viewsets.ModelViewSet):
	queryset = Autor.objects.all()
	serializer_class = AuthorSerializer