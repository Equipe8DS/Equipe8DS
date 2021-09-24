import telebot
import time

bot_token = '2001769551:AAG0IG0D4t6yqQ9tpTyKmACbBsx7QlKCo9E'

bot = telebot.TeleBot(token=bot_token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(commands=['personagens'])
def send_welcome(message):
	bot.reply_to(message, "Vou te mostrar os amigos !")

bot.polling()