
class BotUtil:
    def gerar_lista_personagens(personagens):
        i = 1
        response = ""
        for personagem in personagens:
            response = response + str(i) + " - " + personagem["nome"] + "\n"
            i = i+1
        return response

    def gerar_dicionario_personagens(list):
        list_dict = {personagem['nome']: personagem for personagem in list}
        return list_dict

    def info_detalhada_personagem(personagem):
        info = 'Nome: ' + personagem['nome'] + '\n' + 'Raça: ' + personagem['raca'] + '\n' + 'Classe: ' + personagem['classe'] + '\n' + 'Tipo: ' + personagem['tipo'] + '\n'
        return info