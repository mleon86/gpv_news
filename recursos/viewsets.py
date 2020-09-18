from rest_framework import viewsets

from .models import Curso, Leccion
from .serializers import CursoSerializer, LeccionSerializer


class CursoViewSet(viewsets.ModelViewSet):
	queryset = Curso.objects.all()
	serializer_class = CursoSerializer

class LeccionViewSet(viewsets.ModelViewSet):
	queryset = Leccion.objects.all()
	serializer_class = LeccionSerializer