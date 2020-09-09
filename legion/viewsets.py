from rest_framework import viewsets

from .models import Organizacion, Persona
from .serializer import OrganizacionSerializer, PersonaSerializer


class OrganizacionViewSet(viewsets.ModelViewSet):
	queryset = Organizacion.objects.all()
	serializer_class = OrganizacionSerializer

class PersonaViewSet(viewsets.ModelViewSet):
	queryset = Persona.objects.all()
	serializer_class = PersonaSerializer