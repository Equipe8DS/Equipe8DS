from django.db.models.query import QuerySet
from bot.serializers import PersonagemSerializer
from bot.serializers import ItemSerializer
from bot.serializers import CidadeSerializer
from django.shortcuts import render
from rest_framework import serializers,viewsets,status
from rest_framework.response import Response 
from bot.models import Personagem
from bot.models import Item
from bot.models import Cidade

class PersonagemViewSet (viewsets.ModelViewSet) : 
    queryset = Personagem.objects.all ()
    serializer_class = PersonagemSerializer
    
    def destroy(self, request, *args, **kwargs):
        personagem = self.get_object ()
        personagem.ativo = False
        personagem.save ()
        return Response ({'status': status.HTTP_200_OK})

class ItemViewSet(viewsets.ModelViewSet) :
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def destroy(self, request, *args, **kwargs):
        item = self.get_object ()
        item.ativo = False
        item.save ()
        return Response ({'status': status.HTTP_200_OK})

    def update(self, request, *args, **kwargs):
        item = self.get_object ()
        data = request.data
        item.descricao = data["descricao"]
        item.preco_sugerido = data["preco_sugerido"]
        item.save()
        return Response ({'status': status.HTTP_200_OK, 'descricao': item.descricao, 'preco_sugerido': item.preco_sugerido})

class CidadeViewSet(viewsets.ModelViewSet) :
    queryset = Cidade.objects.all()
    serializer_class = CidadeSerializer

    def destroy(self, request, *args, **kwargs):
        cidade = self.get_object ()
        cidade.ativo = False
        cidade.save ()
        return Response ({'status': status.HTTP_200_OK})            