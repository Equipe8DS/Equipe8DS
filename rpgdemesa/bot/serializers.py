from bot.models import Personagem
from bot.models import Item
from bot.models import Cidade
from rest_framework import serializers

class PersonagemSerializer (serializers.HyperlinkedModelSerializer) :
    dono = serializers.HiddenField (default = serializers.CurrentUserDefault ())

    class Meta : 
        model = Personagem 
        fields = ['nome', 'raca', 'classe', 'tipo', 'ativo', 'dono']

class ItemSerializer (serializers.HyperlinkedModelSerializer) :
    class Meta:
        model = Item
        fields = ['nome', 'preco_sugerido', 'qualidade', 'categoria', 'descricao', 'ativo']

class CidadeSerializer (serializers.HyperlinkedModelSerializer) :
    class Meta:
        model = Cidade
        fields = ['nome_cidade','tesouro','governante','ativo']              
