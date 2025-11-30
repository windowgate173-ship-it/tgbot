import sqlite3, time, random
from random import randint

import telebot
from telebot import TeleBot

token = '8556755260:AAEeMxd4Scw_NIYgYV60Lw76TTHrOQk-lQ4'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    conn = sqlite3.connect('quasi.sql')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key, name varchar(50), pass varchar(50))')

    conn.commit()
    cur.close()
    conn.close()
    bot.send_message(message.chat.id, "Сейчас зарегистрирую! Введи своё имя")
    bot.register_next_step_handler(message, user_name)

def user_name(message):
    global user_name
    name = message.text.strip()
    bot.send_message(message.chat.id, "Введите пароль")
    bot.register_next_step_handler(message, drowssap)

def drowssap(message):
    drowssap = message.text.strip()

    conn = sqlite3.connect('quasi.sql')
    cur = conn.cursor()
    cur.execute("INSERT INTO users (name, pass) VALUES ('%s','%s')" % (user_name, drowssap))

    conn.commit()
    cur.close()
    conn.close()

    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton( 'Список пользователей', callback_data = 'users'))

    bot.send_message(message.chat.id, 'Пользователь зарегистрирован', reply_markup = markup)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    conn = sqlite3.connect('quasi.sql')
    cur = conn.cursor()

    cur.execute('SELECT * FROM users')
    users = cur.fetchall()

    info = ''
    for el in users:
        info += f'Имя: {el[1]}, пароль: {el[2]}\n'

    conn.commit()
    cur.close()
    conn.close()


@bot.message_handler(commands=['alternate'])
def alternate(message):
    conn = sqlite3.connect('quasi.sql')
    cur = conn.cursor()
    cur.execute('ADD COLUMN IF NOT EXISTS role (id int default 0')

    conn.commit()
    cur.close()
    conn.close()
    bot.send_message(message.chat.id, "Добавлен новый столбец")



bot.polling()