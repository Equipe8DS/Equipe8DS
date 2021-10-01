from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from bot.models import Cidade, Jogador
from bot.models import Item
from bot.models import Personagem
from bot.models import Loja
from bot.models import ItemPersonagem

class PersonagemSerializer(serializers.HyperlinkedModelSerializer):
    dono = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Personagem
        fields = ['pk', 'nome', 'raca', 'classe', 'tipo', 'ativo', 'dono']
        depth = 1

class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ['pk', 'nome', 'preco_sugerido', 'qualidade', 'categoria', 'descricao', 'ativo']


class ItemPersonagemSerializer(serializers.ModelSerializer):
    item_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Item.objects.all(), source='item')
    item = ItemSerializer(read_only=True)
    personagem_id = serializers.PrimaryKeyRelatedField(queryset=Personagem.objects.all(), source='personagem')
    
    class Meta:
        model = ItemPersonagem
        fields = ['pk', 'item_id', 'item', 'personagem_id', 'quantidade']
        depth = 1


class CidadeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cidade
        fields = ['pk', 'nome', 'tesouro', 'governante', 'ativo']


class JogadorSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(write_only=True, style={'input_type': 'password', 'placeholder': 'Senha'})

    class Meta:
        model = Jogador
        fields = ['pk', 'nome', 'is_active', 'email', 'password', 'username']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(JogadorSerializer, self).create(validated_data)

class LojaSerializer(serializers.HyperlinkedModelSerializer) :
    class Meta :
        model = Loja
        fields = ['nome', 'responsavel', 'cidade', ]
