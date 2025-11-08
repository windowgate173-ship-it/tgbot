import telebot, random
from telebot import TeleBot

# @tokencharm

token = '8556755260:AAEeMxd4Scw_NIYgYV60Lw76TTHrOQk-lQ4'
bot = telebot.TeleBot(token)

citatstalin = [
    'У каждой проблемы есть ФИО',
    'Самые испорченные люди больше всего тянутся к власти',
    'Если нас ругают враги, мы всё делаем правильно',
    'Чтобы знать, надо учиться'
]

cointhrow = (
    'орёл',
    'решка'
)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Я твой бот-помощник!")

@bot.message_handler(commands=['helping'])
def helping(message):
    bot.send_message(message.chat.id,"Сейчас помогу! Список команд: /start\n /helping\n /quote\n /throw_a_coin" )

@bot.message_handler(commands=['quote'])
def quote(message):
    bot.send_message(message.chat.id, random.choice(citatstalin))

@bot.message_handler(commands=['throw_a_coin'])
def throw_a_coin(message):
    bot.send_message(message.chat.id, random.choice(cointhrow))

@bot.message_handler(content_types=['text'])
def handle_text(message):
    text = message.text.lower()
    if text == "привет":
        bot.send_message(message.chat.id, "Здравствуй, пользователь!")



bot.polling()