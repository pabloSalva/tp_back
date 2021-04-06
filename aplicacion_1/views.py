from django.http import response
from rest_framework import viewsets

from .models import Persona, PersonaEP, Evento
from .serializers import EventoSerializer, PersonaEPSerializer, PersonaSerializer


class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer


class PersonaEPViewSet(viewsets.ModelViewSet):
    queryset = PersonaEP.objects.all()
    serializer_class = PersonaEPSerializer


class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer
