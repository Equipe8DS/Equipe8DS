from bot.serializers import PersonagemSerializer
from django.shortcuts import render
from rest_framework import serializers,viewsets
from bot.models import Personagem

class PersonagemViewSet (viewsets.ModelViewSet) : 
    queryset = Personagem.objects.all ()
    serializer_class = PersonagemSerializer