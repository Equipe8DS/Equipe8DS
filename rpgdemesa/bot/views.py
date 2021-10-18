from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpRequest
from django.http.response import JsonResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from bot.models import Cidade, Jogador
from bot.models import Estoque
from bot.models import Item
from bot.models import ItemPersonagem
from bot.models import Loja
from bot.models import Personagem
from bot.models import Historico
from bot.models import EstiloVida
from bot.models import GastosSemanais
from bot.serializers import CidadeSerializer, JogadorSerializer
from bot.serializers import EstoqueSerializer
from bot.serializers import ItemPersonagemSerializer
from bot.serializers import ItemSerializer
from bot.serializers import LojaSerializer
from bot.serializers import PersonagemSerializer
from bot.serializers import HistoricoSerializer
from bot.serializers import EstiloVidaSerializer
from bot.serializers import GastosSemanaisSerializer

@api_view(['PUT'])
def remover_item_inventario(request, pk):
    try:
        item_personagem = ItemPersonagem.objects.get(pk=pk)
    except ItemPersonagem.DoesNotExist:
        return JsonResponse({'message': 'O item não está no inventário.'}, status=status.HTTP_404_NOT_FOUND)

    item_personagem_data = JSONParser().parse(request)
    item_personagem_serializer = ItemPersonagemSerializer(
        item_personagem, data=item_personagem_data)

    if item_personagem_serializer.is_valid():
        if item_personagem_serializer.data['quantidade'] <= 0:
            item_personagem.delete()
        else:
            item_personagem_serializer.save()
        return JsonResponse(item_personagem_serializer.data)
    return JsonResponse(item_personagem_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ItemPersonagemViewSet(viewsets.ModelViewSet):
    queryset = ItemPersonagem.objects.all()
    serializer_class = ItemPersonagemSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['personagem_id']

    @action(methods=['post'], permission_classes=[permissions.IsAuthenticated], url_path='add-item-inventario',
            url_name='add_item_inventario', detail=False)
    def add_item_inventario(self, request):
        id_personagem = request.data['idPersonagem']
        id_item = request.data['idItem']
        quantidade = int(request.data['quantidade'])
        try:
            inventario = ItemPersonagem.objects.get(
                personagem=id_personagem, item=id_item)
            inventario.quantidade += quantidade
            inventario.save()
            historico = Historico(
                personagem_id=id_personagem, item_id=id_item, quantidade=quantidade, tipo='inclusao')
            historico.save()
            return JsonResponse({'message': 'Item adicionado ao inventário', 'quantidade': inventario.quantidade},
                                status=status.HTTP_200_OK)

        except ObjectDoesNotExist:
            personagem = Personagem.objects.get(pk=id_personagem)
            item = Item.objects.get(pk=id_item)
            inventario = ItemPersonagem(personagem=personagem, item=item,
                                        quantidade=quantidade)
            inventario.save()
            historico = Historico(
                personagem_id=id_personagem, item_id=id_item, quantidade=quantidade, tipo='inclusao')
            historico.save()
            return JsonResponse({'message': 'Item adicionado ao inventário'}, status=status.HTTP_201_CREATED)

    @action(methods=['post'], permission_classes=[permissions.IsAuthenticated], url_path='remover-item-inventario',
            url_name='remover_item_inventario', detail=False)
    def remover_item_inventario(self, request):
        id_personagem = request.data['idPersonagem']
        id_item = request.data['idItem']
        quantidade = int(request.data['quantidade'])

        item_personagem = ItemPersonagem.objects.get(
            personagem=id_personagem, item=id_item)
        nova_quantidade = item_personagem.quantidade - quantidade

        if nova_quantidade > 0:
            item_personagem.quantidade = nova_quantidade
            item_personagem.save()
        elif nova_quantidade == 0:
            if(item_personagem.item.nome != 'Ouro'):
                item_personagem.delete()
        else:
            return JsonResponse({'message': 'Não é possível remover essa quantidade de itens'},
                                status=status.HTTP_403_FORBIDDEN)
        historico = Historico(
            personagem_id=id_personagem, item_id=id_item, quantidade=quantidade, tipo='remocao')
        historico.save()
        return JsonResponse({'message': 'Item removido do inventário'}, status=status.HTTP_200_OK)


class PersonagemViewSet(viewsets.ModelViewSet):
    queryset = Personagem.objects.all()
    serializer_class = PersonagemSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['nome']

    def destroy(self, request, *args, **kwargs):
        personagem = self.get_object()
        personagem.ativo = False
        personagem.save()
        return Response({'status': status.HTTP_200_OK})


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['nome']

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
    filterset_fields = ['nome']

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

    @action(methods=['post'], permission_classes=[permissions.IsAuthenticated], url_path='comprar-item',
            url_name='comprar_item', detail=False)
    def comprar_item(self, request):
        id_loja = request.data['idLoja']
        id_item = request.data['idItem']
        quantidade = int(request.data['quantidade'])

        try:
            estoque = Estoque.objects.get(loja=id_loja, item=id_item)
            personagem = Personagem.objects.get(id=request.data['idPersonagem'])
        except ObjectDoesNotExist:
            return JsonResponse({'message': 'Este item não está mais disponível'}, status=status.HTTP_404_NOT_FOUND)

        gold_personagem = personagem.itempersonagem_set.get(
            item=Item.objects.get(nome='Ouro'))

        valor_compra = estoque.preco_item * quantidade
        personagem_has_gold = gold_personagem.quantidade >= valor_compra
        loja_has_estoque = estoque.quantidade_item >= quantidade

        if personagem_has_gold and loja_has_estoque:
            request_remove_estoque = HttpRequest()
            request_remove_estoque.data = {
                'idLoja': id_loja, 'idItem': id_item, 'quantidade': quantidade}
            EstoqueViewSet.remove_item_loja(
                EstoqueViewSet(), request=request_remove_estoque)
            try:
                request_add_inventario = HttpRequest()
                request_add_inventario.data = {'idPersonagem': personagem.id, 'idItem': id_item,
                                               'quantidade': quantidade}
                ItemPersonagemViewSet.add_item_inventario(
                    ItemPersonagemViewSet(), request=request_add_inventario)

                request_remove_gold = HttpRequest()
                request_remove_gold.data = {'idPersonagem': personagem.id, 'idItem': gold_personagem.item.id,
                                            'quantidade': valor_compra}
                ItemPersonagemViewSet.remover_item_inventario(ItemPersonagemViewSet(),
                                                              request=request_remove_gold)

            except ObjectDoesNotExist:
                personagem.itempersonagem_set.create(
                    item_id=id_item, quantidade=quantidade)
                personagem.save()

            historico = Historico(
                personagem_id=personagem.id, item_id=id_item, quantidade=quantidade, tipo='compra', preco=valor_compra, loja_id=id_loja)
            historico.save()

            return JsonResponse({'message': f'Compra efetuada. {quantidade} unidade(s) do item {estoque.item.nome} foram compradas pelo valor de {valor_compra} peças de ouro.'}, status=status.HTTP_200_OK)
        else:
            return JsonResponse({'message': 'Compra não autorizada.', 'lojaHasEstoque': loja_has_estoque,
                                 'personagemHasGold': personagem_has_gold}, status=status.HTTP_200_OK)

    def comprar_por_tipo(self, gastoSemanal, dinheiro_total, idPersonagem):
        carrinho_compras = []
        dinheiro_atual = dinheiro_total
        consegue_comprar = True

        while(consegue_comprar):
            estoques = Estoque.objects.all()
            comprou_algo = False
            for estoque in estoques:
                if estoque.item.categoria == gastoSemanal.tipo:
                    if(dinheiro_atual >= estoque.preco_item):
                        carrinho_compras.append({'lojaId': estoque.loja.id, 'itemId': estoque.item.id}) 
                        dinheiro_atual = dinheiro_atual - estoque.preco_item
                        comprou_algo = True

            for compra in carrinho_compras:
                request_comprar = HttpRequest()
                request_comprar.data = {'idLoja': compra['lojaId'], 'idItem': compra['itemId'], 'quantidade': 1, 'idPersonagem': idPersonagem}
                print(request_comprar.data)
                retorno = self.comprar_item(request=request_comprar)

            if(dinheiro_atual == 0 or comprou_algo == False):
                consegue_comprar = False

            carrinho_compras = []

    @action(methods=['post'], permission_classes=[permissions.IsAuthenticated], url_path='realizar_compras_semanais',
            url_name='realizar_compras_semanais', detail=False)
    def realizar_compras_semanais(self, request):
        
        try:
            personagens = Personagem.objects.filter(tipo='npc')

            for personagem in personagens:
                renda = personagem.getOuro()
                gastosSemanais = GastosSemanais.objects.filter(estiloVida = personagem.estiloVida)

                gastos_por_tipo = {}

                for gastoSemanal in gastosSemanais:
                    gastos_por_tipo[gastoSemanal.tipo] = renda * (gastoSemanal.gastoPercentual / 100)

                for gastoSemanal in gastosSemanais:
                    self.comprar_por_tipo(gastoSemanal, gastos_por_tipo[gastoSemanal.tipo], personagem.id)

            return JsonResponse({'message': 'Compras efetuadas'},
                                status=status.HTTP_200_OK)
        except ObjectDoesNotExist as e:
            print(e)
            return JsonResponse({'message': 'Erro ao efetuar compra'},
                                    status=status.HTTP_200_OK)   

class EstoqueViewSet(viewsets.ModelViewSet):
    queryset = Estoque.objects.all()
    serializer_class = EstoqueSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['loja_id']

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
            preco = float(request.data['preco']) if (
                'preco' in request.data) else item.preco_sugerido

            estoque = Estoque(loja=loja, item=item,
                              quantidade_item=quantidade, preco_item=preco)
            estoque.save()
            return JsonResponse({'message': 'Item adicionado ao estoque'}, status=status.HTTP_201_CREATED)

    @action(methods=['post'], permission_classes=[permissions.IsAuthenticated], url_path='remove-item-loja',
            url_name='remove_item_loja', detail=False)
    def remove_item_loja(self, request):
        id_loja = request.data['idLoja']
        id_item = request.data['idItem']
        quantidade = int(request.data['quantidade'])
        estoque = Estoque.objects.get(loja=id_loja, item=id_item)
        nova_quantidade = estoque.quantidade_item - quantidade

        if nova_quantidade > 0:
            estoque.quantidade_item = nova_quantidade
            estoque.save()
        elif nova_quantidade == 0:
            estoque.delete()

        else:
            return JsonResponse({'message': f'Não é possível remover {quantidade} itens, '
                                            f'essa loja possui apenas {estoque.quantidade_item}.'},
                                status=status.HTTP_401_UNAUTHORIZED)

        return JsonResponse({'message': 'Item removido do estoque'}, status=status.HTTP_200_OK)


class HistoricoViewSet (viewsets.ModelViewSet):
    queryset = Historico.objects.all()
    serializer_class = HistoricoSerializer
    permission_classes = [permissions.IsAuthenticated]

class EstiloVidaViewSet (viewsets.ModelViewSet):
    queryset = EstiloVida.objects.all()
    serializer_class = EstiloVidaSerializer
    permission_classes = [permissions.IsAuthenticated]

class GastosSemanaisViewSet (viewsets.ModelViewSet):
    queryset = GastosSemanais.objects.all()
    serializer_class = GastosSemanaisSerializer
    permission_classes = [permissions.IsAuthenticated]