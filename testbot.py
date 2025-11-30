import telebot
from telebot import TeleBot

# @Token_Charm_bot

token = '8556755260:AAEeMxd4Scw_NIYgYV60Lw76TTHr0Qk-104'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Я твой бот-помощник!")

bot.polling()