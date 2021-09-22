from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from bot.models import Cidade, Jogador
from bot.models import Item
from bot.models import Personagem


class PersonagemSerializer(serializers.HyperlinkedModelSerializer):
    dono = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Personagem
        fields = ['nome', 'raca', 'classe', 'tipo', 'ativo', 'dono']


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ['nome', 'preco_sugerido', 'qualidade', 'categoria', 'descricao', 'ativo']


class CidadeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cidade
        fields = ['nome_cidade', 'tesouro', 'governante', 'ativo']


class JogadorSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(write_only=True, style={'input_type': 'password', 'placeholder': 'Senha'})

    class Meta:
        model = Jogador
        fields = ['nome', 'is_active', 'email', 'password', 'username']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(JogadorSerializer, self).create(validated_data)
