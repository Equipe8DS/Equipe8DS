import json
import requests
import os
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth

class BotController:
    def buscar_personagens():
        load_dotenv()

        request = requests.get(os.getenv('URL_API'), auth=(os.getenv('LOGIN'), os.getenv('PASSW')))
        a_json_object = json.loads(request.content)
        list_from_json = a_json_object["results"]
        return list_from_json