from rest_framework import viewsets, status, permissions
from rest_framework.response import Response

from bot.models import Cidade, Jogador
from bot.models import Item
from bot.models import Personagem
from bot.serializers import CidadeSerializer, JogadorSerializer
from bot.serializers import ItemSerializer
from bot.serializers import PersonagemSerializer


class PersonagemViewSet(viewsets.ModelViewSet):
    queryset = Personagem.objects.all()
    serializer_class = PersonagemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        personagem = self.get_object()
        personagem.ativo = False
        personagem.save()
        return Response({'status': status.HTTP_200_OK})


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        item = self.get_object()
        item.ativo = False
        item.save()
        return Response({'status': status.HTTP_200_OK})

    def update(self, request, *args, **kwargs):
        item = self.get_object()
        data = request.data
        item.descricao = data["descricao"]
        item.preco_sugerido = data["preco_sugerido"]
        item.save()
        return Response(
            {'status': status.HTTP_200_OK, 'descricao': item.descricao, 'preco_sugerido': item.preco_sugerido})


class CidadeViewSet(viewsets.ModelViewSet):
    queryset = Cidade.objects.all()
    serializer_class = CidadeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        cidade = self.get_object()
        cidade.ativo = False
        cidade.save()
        return Response({'status': status.HTTP_200_OK})


class JogadorViewSet(viewsets.ModelViewSet):
    queryset = Jogador.objects.all()
    serializer_class = JogadorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAuthenticated]

        return [permission() for permission in permission_classes]

    def destroy(self, request, *args, **kwargs):
        jogador = self.get_object()
        jogador.is_active = False
        jogador.save()
        return Response({'status': status.HTTP_200_OK})
