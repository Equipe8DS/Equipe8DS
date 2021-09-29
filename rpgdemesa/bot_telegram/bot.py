import telebot
from telebot import types
import time
import os
from dotenv import load_dotenv
from botUtil import BotUtil
from botController import BotController

load_dotenv()

bot_token = os.getenv('BOT_TOKEN')

bot = telebot.TeleBot(token=bot_token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    cid = message.chat.id
    bot.send_chat_action(cid, 'typing')
    bot.reply_to(message, "Seja bem-vindo ! A grande Redzay te espera.")

@bot.message_handler(commands=['personagens'])
def send_personagens_lista(message):
    cid = message.chat.id
    results = BotController.buscar_personagens()
    response = BotUtil.gerar_lista_por_nomes(results)
    bot.send_chat_action(cid, 'typing')
    bot.reply_to(message, "Personagens registrados: \n" + response, parse_mode="Markdown")

@bot.message_handler(commands=['personagem'])
def send_info_personagem(message):
    cid = message.chat.id
    results = BotController.buscar_personagens()
    response_dict = BotUtil.gerar_dicionario_lista_por_nome(results)

    personagem_name = ' '.join(message.text.split(' ')[1:])

    if not personagem_name:
        bot.send_chat_action(cid, 'typing')
        bot.send_message(cid, "Insira o nome do personagem que deseja visualizar.")
    else:
        try:
            info = BotUtil.info_detalhada_personagem(response_dict[personagem_name])
            bot.send_chat_action(cid, 'typing')
            bot.send_message(cid, info, parse_mode="Markdown")
        except:
            bot.send_chat_action(cid, 'typing')
            bot.send_message(cid, "Houve um erro ao consultar o personagem.", parse_mode="Markdown")

@bot.message_handler(commands=['itens'])
def send_itens_lista(message):
    cid = message.chat.id
    results = BotController.buscar_itens()
    response = BotUtil.gerar_lista_por_nomes(results)
    bot.send_chat_action(cid, 'typing')
    bot.reply_to(message, "Itens registrados: \n" + response, parse_mode="Markdown")

@bot.message_handler(commands=['item'])
def send_info_item(message):
    cid = message.chat.id
    results = BotController.buscar_itens()
    response_dict = BotUtil.gerar_dicionario_lista_por_nome(results)

    item_name = ' '.join(message.text.split(' ')[1:])
    
    if not item_name:
        bot.send_chat_action(cid, 'typing')
        bot.send_message(cid, "Insira o nome do item que deseja visualizar.")
    else:
        try:
            info = BotUtil.info_detalhada_item(response_dict[item_name])
            bot.send_chat_action(cid, 'typing')
            bot.send_message(cid, info, parse_mode="Markdown")
        except Exception as e:
            print(e)
            bot.send_chat_action(cid, 'typing')
            bot.send_message(cid, "Houve um erro ao consultar o item.", parse_mode="Markdown")

@bot.message_handler(commands=['cidades'])
def send_cidades_lista(message):
    cid = message.chat.id
    results = BotController.buscar_cidade()
    response = BotUtil.gerar_lista_por_nomes(results)
    bot.send_chat_action(cid, 'typing')
    bot.reply_to(message, "Cidades registradas: \n" + response, parse_mode="Markdown")

@bot.message_handler(commands=['cidade'])
def send_info_item(message):
    cid = message.chat.id
    results = BotController.buscar_cidade()
    response_dict = BotUtil.gerar_dicionario_lista_por_nome(results)

    cidade_name = ' '.join(message.text.split(' ')[1:])
    
    if not cidade_name:
        bot.send_chat_action(cid, 'typing')
        bot.send_message(cid, "Insira o nome da cidade que deseja visualizar.")
    else:
        try:
            info = BotUtil.info_detalhada_cidade(response_dict[cidade_name])
            bot.send_chat_action(cid, 'typing')
            bot.send_message(cid, info, parse_mode="Markdown")
        except Exception as e:
            print(e)
            bot.send_chat_action(cid, 'typing')
            bot.send_message(cid, "Houve um erro ao consultar a cidade.", parse_mode="Markdown")

bot.polling()

#while True:
#    try:
#        bot.polling()
#    except Exception:
#        time.sleep(15)