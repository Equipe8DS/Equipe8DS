import requests

def buscar_personagens():
    request = requests.get("http://localhost:8000/personagens")
    print(request.content)

if __name__ == '__main__':
    buscar_personagens()