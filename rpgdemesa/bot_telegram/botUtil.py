from botController import BotController
class BotUtil:
    def gerar_lista_por_nomes(list):
        i = 1
        response = ""
        for object in list:
            response = response + str(i) + " - " + object["nome"] + "\n"
            i = i+1
        return response

    def gerar_dicionario_lista_por_nome(list):
        list_dict = {object['nome']: object for object in list}
        return list_dict

    def gerar_dicionario_lista_por_nome_itens_estoque(list):
        list_dict = {object['item']['nome']: object for object in list}
        return list_dict

    def info_detalhada_personagem(personagem):
        info = 'Nome: ' + personagem['nome'] + '\n' + 'Raça: ' + personagem['raca'] + '\n' + 'Classe: ' + personagem['classe'] + '\n' + 'Tipo: ' + personagem['tipo'] + '\n'
        return info

    def info_detalhada_item(item):
        info = 'Nome: ' + item['nome'] + '\n' + 'Preço Sugerido: ' + str(item['preco_sugerido']) + ' peças de ouro' + '\n' + 'Qualidade: ' + BotUtil.imprime_qualidade(item['qualidade']) + '\n' + 'Categoria: ' + BotUtil.imprime_categoria(item['categoria']) + '\n' + 'Descrição: ' + item['descricao'] + '\n'
        return info


    def info_detalhada_cidade(cidade):
        info = 'Nome: ' + cidade['nome'] + '\n' + 'Tesouro: ' + str(cidade['tesouro']) + ' peças de ouro' + '\n'
        return info

    def imprime_qualidade(qualidade):
        if(qualidade == 'ruim'):
            return 'Ruim'
        elif(qualidade == 'pobre'):
            return 'Pobre'
        elif(qualidade == 'medio'):
            return 'Médio'
        elif(qualidade == 'bom'):
            return 'Bom'
        elif(qualidade == 'excelente'):
            return 'Excelente'

    def imprime_categoria(categoria):
        if(categoria == 'alimentos'):
            return 'Alimentos'
        elif(categoria == 'transporte'):
            return 'Transporte'
        elif(categoria == 'academico'):
            return 'Acadêmico'
        elif(categoria == 'agricultura'):
            return 'Agricultura'
        elif(categoria == 'casa'):
            return 'Casa'
        elif(categoria == 'equipamento'):
            return 'Equipamento'
        elif(categoria == 'luxo'):
            return 'Luxo'

    def info_detalhada_jogador(jogador):
        info = 'Nome: ' + jogador['nome'] + '\n' + 'E-mail: ' + str(jogador['email']) + '\n'  + 'Username: ' + str(jogador['username']) + '\n'
        return info

    def info_detalhada_loja(loja):
        info = 'Nome: ' + loja['nome'] + '\n' + 'Cidade: ' + str(loja['cidade']) + '\n'  + 'Responsável: ' + str(loja['responsavel']) + '\n' + 'Ativo: ' + str(loja['ativo']) + '\n'
        return info

    def info_detalhada_estoque(loja):
        id = loja['pk']

        results = BotController.buscar_estoque(id)
        response_dict = BotUtil.gerar_dicionario_lista_por_nome_itens_estoque(results)

        info = ""

        for key in response_dict:
            elem = response_dict[key]
            item = elem['item']
            info = info + 'Nome: ' + item['nome'] + '\n' + 'Qualidade: ' + BotUtil.imprime_qualidade(item['qualidade']) + '\n' + 'Categoria: ' + BotUtil.imprime_categoria(item['categoria']) + '\n' + 'Descrição: ' + item['descricao'] + '\n'
            info = info + 'Preço:' + str(elem['preco_item']) + ' peças de ouro ' + '\n'  + 'Quantidade: ' + str(elem['quantidade_item']) + '\n'
            info = info + '\n' + '\n'

        return info