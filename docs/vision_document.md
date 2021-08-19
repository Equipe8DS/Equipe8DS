# Documento de Visão

## Histórico de Versão
| Data | Versão | Descrição | Autor |
| :--- | :--- | :--- | :--- |
| 18/08| 0.1 | Adicionado Introdução| João Vitor, João Pedro, Lucas Midley e Lucas Oliveira |
| 18/08| 0.2 | Adicionado Descrição do Usuário, Envolvidos e Referências| João Vitor |
| 18/08| 0.2.1 | Adicionada a ocupação dos Envolvidos| João Vitor |
| 19/08| 0.3 | Adicionado Recursos do Produto| João Pedro |

## Sumário
[1. Introdução](#1-introdução)
* [1.1 Sobre o RPG de mesa](#11-sobre-o-rog-de-mesa)
* [1.2 Objetivo](#12-objetivo)
* [1.3 Visão Geral da Solução](#13-visão-geral-da-solução)

[2. Descrição do Usuário](#2-descrição-do-usuário)
* [2.1 Tipos de Usuário](#21-tipos-de-usuário)
* [2.2 Principais Necessidades do Usuário](#22-principais-necessidades-do-usuário)
* [2.3 Ambiente do Usuário](#23-ambiente-do-usuário)
* [2.4 Alternativas e Competição](#24-alternativas-e-competição)

[3. Envolvidos](#3-envolvidos)

[5. Recursos do produto](#5-recursos-do-produto)

[6. Referências](#6-referências)

## 1. Introdução

Este documento tem o objetivo de definir os aspectos relevantes do projeto e levantar os requisitos necessários para executá-lo.
A ideia base deste projeto consiste na criação de um _chatbot_ que automatize um dos aspectos de um RPG de mesa utilizando a plataforma de serviço de mensagens instantâneas _Telegram_.

### 1.1 Sobre o RPG de mesa

O RPG (do inglês, _Role Playing Game_) de mesa é um genêro jogo colaborativo em que os jogadores assumem papéis de personagens em um ambiente imaginário para criar uma história seguindo regras e diretrizes pré-definidas. As partidas, normalmente, ocorrem em sessões em que esses jogadores se reúnem para jogar. 

Além disso, é possível realizar ações durante essas sessões, como comprar e/ou usar itens e aprender uma nova habilidade, por exemplo. Nesses casos, os jogadores precisam conversar com o Mestre para saber se é possível efetivar as ações desejadas. Tendo isso em vista, a dependência do Mestre para a execução do jogo, pode, em certo momento, de acordo com a quantidade de ações e/ou jogadores, gerar um sobrecarregamento no Mestre.

### 1.2 Objetivo

Este projeto tem como objetivo central facilitar o gerenciamento de trocas de itens feitas pelos jogadores no intervalo entre as sessões.

Atualmente, toda a gerência de estoque de lojas dos NPCs (_Non-Playable Character_, isto é, personagens não jogáveis) e coleta de impostos na cidade onde o jogo se passa, é feita pelo Mestre, o que acarreta em demora no tempo de resposta e erros.

### 1.3 Visão Geral da Solução

O propósito do _chatbot_ é automatizar o processo de compra e venda de itens entre os jogadores e os NPCs, além de gerar um relatório das transações para o Mestre. O sistema também será responsável pela troca de itens entre os NPCs e por fazer a coleta de impostos destes, a fim de aproximar a economia do jogo ao mundo real.

| O problema da| Centralização de tarefas|
| :--- | :---: |
| Afeta | Os jogadores e, principalmente, o Mestre. |
| Cujo impacto é | O atraso da resposta e possíveis erros por parte do Mestre |
| Uma boa solução seria | Um _chatbot_ que reduza as responsabilidades do Mestre|

## 2. Descrição do Usuário
Os usuários do chatbot serão jogadores de RPG de mesa de vários estados do Brasil, com idades entre 15 a 29 anos.

### 2.1 Tipos de Usuário
|Tipo | Descrição | Restrição de Acesso |
| :--- | :--- | :--- |
| Jogadores | Interpretam personagens | Não possuem acesso ao histórico de transações (compra e venda de itens) do jogo e ao inventário dos vendedores |
| Mestre | Narrador do jogo, quem cria a história |

### 2.2 Principais Necessidades do Usuário
| Necessidade | Prioridade | Interesses | Solução atual | Solução proposta
| --- | --- | --- | --- | --- |
| Compra e venda de itens | Alta | Manter o andamento do jogo, suprindo as necessidades pontuais do personagem | Mestre comanda o comércio, verificando a disponibilidade do produto | _Chatbot_ para realizar as operações comerciais solicitadas pelos jogadores
| Gerar um relatório de transações | Alta | Manter o Mestre informado a respeito da situação econômica do jogo | O Mestre utiliza uma planilha de preenchemento manual e precisa estar sempre a atualizando | O _chatbot_ gera um relatório sobre todas as operações realizadas, ao final do dia
| Cobrança de impostos | Baixa | Assemelhar a economia do jogo com a do mundo real | Mestre realiza a cobrança de cada jogador | _Chatbot_ para realizar as movimentações tributárias do jogo

### 2.3 Ambiente do Usuário
O _chatbot_ será desenvolvido para aumentar a comodidade dos jogadores de RPG de mesa e simplificar a atuação do Mestre nas sessões.

### 2.4 Alternativas e Competição
Nesta seção são descritos competidores ou alternativas ao aplicativo que está sendo criado. No entanto, após pesquisas, nenhuma solução foi encontrada para o problema descrito neste documento.


## 3. Envolvidos
|Nome | Ocupação |
| :--- | :--- |
| Caio Felipe Dias Nunes | Equipe de Desenvolvimento |
| João Pedro Macedo Faria | Equipe de Desenvolvimento |
| João Vitor de Souza Durco | Equipe de Desenvolvimento |
| Leonardo Ferreira Borges | Equipe de Desenvolvimento |
| Lucas Leite Macedo Maduro | Equipe de Desenvolvimento |
| Lucas Midlhey Cardoso Naves | Equipe de Desenvolvimento |
| Lucas Oliveira Silva | Equipe de Desenvolvimento |


## 4. Visão geral do produto
O objetivo principal do aplicativo é facilitar as ações do mestre, visto que o bot irá automatizar o processo de comprar e vender itens, além de que o jogador poderá gerenciar o seu próprio inventário, entre outros funcionamentos do RPG de mesa.

### 4.1 Perspectiva do Produto
Espera-se que o bot aperfeiçoe a jogabilidade do RPG de mesa, já que suas funções vão diminuir a carga do mestre, com recursos que serão feitos de forma automática pelo bot.

### 4.2 Declaração de Posição do Produto
| Para | Jogadores do RPG de mesa
| --- | :--- |
| Que | Queiram facilitar as ações do mestre. |
| O | sistema |
| Que | Promove melhor jogabilidade entre os jogadores. |
|Ao Contrário | Da aplicação atual, que o mestre é responsável pela maior parte das ações e, consequentemente, fica sobrecarregado. |
| Nosso Produto | Permite que os jogadores realizem ações sem depender exclusivamente do mestre, contribuindo para o RPG de mesa.


## 5. Recursos do produto

O sistema de _chatbot_ irá fornecer as seguintes funcionalidades ao jogador:
* **Visualizar Itens -** Permite o jogador visualizar os itens vendidos por cada NPC.
* **Visualizar NPCs -** Permite o jogador visualizar quais NPCs estão disponíveis.
* **Botão Comprar/Vender -** Permite que o jogador solicite a compra e/ou venda de itens.

O sistema de _chatbot_ irá fornecer as seguintes funcionalidades ao mestre:
* **Busca de itens -** Permite o mestre consultar informações referentes a qualquer item.
* **Busca de NPCs -** Permite o mestre consultar informações referentes a qualquer NPC.
* **Busca de Relatórios -** Permite o mestre consultar informações referentes a relatórios pré existentes.

O sistema de _chatbot_ terá as seguintes funcionalidades:
* **Operações de troca -** Permite a realização automática de todas as operações de venda e compra dos jogadores.
* **Cobrança de impostos -** Permite a realização automática de todas as operações tributárias.
* **Relatórios de transações-** Permite a geração de relatórios das transações e da cobrança de impostos.

## 6. Referências
ZOOM. Redação Zoom, 2021. RPG de mesa: o que é? Como jogar? Quais os melhores? Veja o guia!. Disponível em: <https://www.zoom.com.br/jogos/deumzoom/rpg-de-mesa>. Acesso em: 18 de ago. de 2021.
