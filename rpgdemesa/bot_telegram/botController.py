import json
import requests
import os
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth
from typing import Final

class BotController:

    def URL_API():
        return os.getenv('URL_API')

    def LOGIN_AUTH():
        return os.getenv('LOGIN')

    def PASSW_AUTH():
        return os.getenv('PASSW')

    def buscar_personagens():
        load_dotenv()
 
        request = requests.get(BotController.URL_API() + '/personagem/', auth=(BotController.LOGIN_AUTH(), BotController.PASSW_AUTH()))
        a_json_object = json.loads(request.content)
        list_from_json = a_json_object["results"]
        return list_from_json

    def buscar_itens():
        load_dotenv()

        request = requests.get(BotController.URL_API() + '/item/', auth=(BotController.LOGIN_AUTH(), BotController.PASSW_AUTH()))
        print(request)
        a_json_object = json.loads(request.content)
        list_from_json = a_json_object["results"]
        return list_from_json

    def buscar_cidade():
        load_dotenv()

        request = requests.get(BotController.URL_API() + '/cidade/', auth=(BotController.LOGIN_AUTH(), BotController.PASSW_AUTH()))
        print(request)
        a_json_object = json.loads(request.content)
        list_from_json = a_json_object["results"]
        return list_from_json

    def buscar_jogador():
        load_dotenv()

        request = requests.get(BotController.URL_API() + '/jogador/', auth=(BotController.LOGIN_AUTH(), BotController.PASSW_AUTH()))
        print(request)
        a_json_object = json.loads(request.content)
        list_from_json = a_json_object["results"]
        return list_from_json

    def buscar_loja():
        load_dotenv()

        request = requests.get(BotController.URL_API() + '/loja/', auth=(BotController.LOGIN_AUTH(), BotController.PASSW_AUTH()))
        print(request)
        a_json_object = json.loads(request.content)
        list_from_json = a_json_object["results"]
        return list_from_json

    def buscar_estoque(loja_id):
        load_dotenv()

        request = requests.get(BotController.URL_API() + '/estoque/?loja_id=' + str(loja_id), auth=(BotController.LOGIN_AUTH(), BotController.PASSW_AUTH()))
        print(request)
        a_json_object = json.loads(request.content)
        list_from_json = a_json_object["results"]
        return list_from_json

    
    def buscar_loja_nome(loja_nome):
        load_dotenv()

        request = requests.get(BotController.URL_API() + f'/loja/?nome={loja_nome}', auth=(BotController.LOGIN_AUTH(), BotController.PASSW_AUTH()))
        print(request)
        a_json_object = json.loads(request.content)
        list_from_json = a_json_object["results"][0]
        return list_from_json

    def buscar_personagem_nome(personagem_nome):
        load_dotenv()

        request = requests.get(BotController.URL_API() + f'/personagem/?nome={personagem_nome}', auth=(BotController.LOGIN_AUTH(), BotController.PASSW_AUTH()))
        print(request)
        a_json_object = json.loads(request.content)
        list_from_json = a_json_object["results"][0]
        return list_from_json

    def buscar_item_nome(item_nome):
        load_dotenv()

        request = requests.get(BotController.URL_API() + f'/item/?nome={item_nome}', auth=(BotController.LOGIN_AUTH(), BotController.PASSW_AUTH()))
        print(request)
        a_json_object = json.loads(request.content)
        list_from_json = a_json_object["results"][0]
        return list_from_json

    def comprar_item(nomeLoja, nomePersonagem, nomeItem, quantidade):

        load_dotenv()

        idLoja = BotController.buscar_loja_nome(nomeLoja)['pk']
        idPersonagem = BotController.buscar_personagem_nome(nomePersonagem)['pk']
        idItem = BotController.buscar_item_nome(nomeItem)['pk']

        print(idLoja)
        print(idPersonagem)
        print(idItem)

        request = requests.post(BotController.URL_API() + '/loja/comprar-item/',
                                data={'idLoja': idLoja, 'idPersonagem': idPersonagem, 'idItem': idItem, 'quantidade': quantidade},
                                auth=(BotController.LOGIN_AUTH(), BotController.PASSW_AUTH()))
        print(request)
        a_json_object = json.loads(request.content)
        response = a_json_object["message"]
        return response
