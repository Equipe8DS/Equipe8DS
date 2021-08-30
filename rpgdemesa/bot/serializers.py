from bot.models import Personagem
from rest_framework import serializers

class PersonagemSerializer (serializers.HyperlinkedModelSerializer) :
    class Meta : 
        model = Personagem 
        fields = ['nome', 'raca', 'classe', 'tipo']