from django.core.exceptions import ObjectDoesNotExist
from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser

from bot.models import Cidade, Jogador
from bot.models import Item
from bot.models import Personagem
from bot.models import Loja
from bot.models import ItemPersonagem
from bot.models import Estoque
from bot.serializers import CidadeSerializer, JogadorSerializer
from bot.serializers import ItemSerializer
from bot.serializers import PersonagemSerializer
from bot.serializers import ItemPersonagemSerializer
from bot.serializers import LojaSerializer
from bot.serializers import EstoqueSerializer
from rest_framework.decorators import api_view
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action


@api_view(['PUT'])
def remover_item_inventario(request, pk):
    try:
        item_personagem = ItemPersonagem.objects.get(pk=pk)
    except ItemPersonagem.DoesNotExist:
        return JsonResponse({'message': 'O item não está no inventário.'}, status=status.HTTP_404_NOT_FOUND)

    item_personagem_data = JSONParser().parse(request)
    item_personagem_serializer = ItemPersonagemSerializer(item_personagem, data=item_personagem_data)

    if item_personagem_serializer.is_valid():
        if item_personagem_serializer.data['quantidade'] == 0:
            item_personagem.delete()
        else:
            item_personagem_serializer.save()
        return JsonResponse(item_personagem_serializer.data)
    return JsonResponse(item_personagem_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ItemPersonagemViewSet(viewsets.ModelViewSet):
    queryset = ItemPersonagem.objects.all()
    serializer_class = ItemPersonagemSerializer
    # permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['personagem_id']


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


class LojaViewSet(viewsets.ModelViewSet):
    queryset = Loja.objects.all()
    serializer_class = LojaSerializer

    def get_permissions(self):

        if self.action != 'list':
            permission_classes = [permissions.IsAdminUser]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]

    def destroy(self, request, *args, **kwargs):
        loja = self.get_object()
        loja.ativo = False
        loja.save()
        return Response({'status': status.HTTP_200_OK})


class EstoqueViewSet(viewsets.ModelViewSet):
    queryset = Estoque.objects.all()
    serializer_class = EstoqueSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(methods=['post'], permission_classes=[permissions.IsAuthenticated], url_path='add-item-loja',
            url_name='add_item_loja', detail=False)
    def add_item_loja(self, request):
        id_loja = request.data['idLoja']
        id_item = request.data['idItem']
        quantidade = int(request.data['quantidade'])
        try:
            estoque = Estoque.objects.get(loja=id_loja, item=id_item)
            estoque.quantidade_item += quantidade
            estoque.save()
            return JsonResponse({'message': 'Item adicionado ao estoque', 'quantidade': estoque.quantidade_item},
                                status=status.HTTP_200_OK)

        except ObjectDoesNotExist:
            loja = Loja.objects.get(pk=id_loja)
            item = Item.objects.get(pk=id_item)
            preco = float(request.data['preco']) if ('preco' in request.data) else item.preco_sugerido

            estoque = Estoque(loja=loja, item=item, quantidade_item=quantidade, preco_item=preco)
            estoque.save()
            return JsonResponse({'message': 'Item adicionado ao estoque'}, status=status.HTTP_201_CREATED)
