from bot.models import Personagem
from rest_framework import serializers

class PersonagemSerializer (serializers.HyperlinkedModelSerializer) :
    dono = serializers.HiddenField (default = serializers.CurrentUserDefault ())

    class Meta : 
        model = Personagem 
        fields = ['nome', 'raca', 'classe', 'tipo', 'ativo', 'dono']