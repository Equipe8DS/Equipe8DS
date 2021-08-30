from bot.serializers import PersonagemSerializer
from django.shortcuts import render
from rest_framework import serializers,viewsets,status
from rest_framework.response import Response 
from bot.models import Personagem

class PersonagemViewSet (viewsets.ModelViewSet) : 
    queryset = Personagem.objects.all ()
    serializer_class = PersonagemSerializer
    
    def destroy(self, request, *args, **kwargs):
        personagem = self.get_object ()
        personagem.ativo = False
        personagem.save ()
        return Response ({'status': status.HTTP_200_OK})