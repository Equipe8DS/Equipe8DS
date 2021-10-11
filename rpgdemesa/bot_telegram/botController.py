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