from bot.serializers import LojaSerializer
from bot.models import Loja
from bot.serializers import PersonagemSerializer
from django.shortcuts import render
from rest_framework import serializers,viewsets,status
from rest_framework.response import Response 
from bot.models import Personagem
from rest_framework import permissions

class PersonagemViewSet (viewsets.ModelViewSet) : 
    queryset = Personagem.objects.all()
    serializer_class = PersonagemSerializer
    
    def destroy(self, request, *args, **kwargs):
        personagem = self.get_object()
        personagem.ativo = False
        personagem.save ()
        return Response ({'status': status.HTTP_200_OK})

class LojaViewSet (viewsets.ModelViewSet) :
    queryset = Loja.objects.all()
    serializer_class = LojaSerializer
          
    def get_permissions(self):
    
        if self.action != 'list' :
            permission_classes = [permissions.IsAdminUser]
        else :
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]