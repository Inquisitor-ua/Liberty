import telebot
import config
import time
import pyautogui as pg
from telebot import types
import os
import webbrowser as wb
from bs4 import BeautifulSoup
import requests
import db
from sqlite3 import IntegrityError


TOKEN = config.BOT_TOKEN

bot = telebot.TeleBot(TOKEN)

def klava(buttons):
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    for button in buttons:
        markup.add(types.KeyboardButton(button))
    return markup

@bot.message_handler(commands=["start", "home"])
def hello(message):
    markup = klava(["Регистрация"])
    bot.reply_to(message, "Зарегайся", reply_markup=markup)
    
@bot.message_handler(content_types=['text'])
def reg(message):
    if message.text == 'Регистрация':
        markup = klava(['Назад'])
        msg = bot.send_message(message.chat.id, "Введите ваше имя", reply_markup=markup)
        bot.register_next_step_handler(msg, get_name)
    else:
        markup = klava(["Регистрация"])
        bot.send_message(message.chat.id, "Не понял тебя", reply_markup=markup)

def get_name(message):
    if message.text == 'Назад':
        markup = klava(["Регистрация"])
        bot.send_message(message.chat.id, "Зарегайся", reply_markup=markup)
    else:
        markup = klava(['Назад'])
        name = message.text
        msg = bot.send_message(message.chat.id, "Имя принято!\nТеперь фамилия", reply_markup=markup)
        bot.register_next_step_handler(msg, Surname, name)

def Surname(message, name):
    if message.text == 'Назад':
        markup = klava(["Регистрация"])
        bot.send_message(message.chat.id, "Зарегайся", reply_markup=markup)
    else:
        surname = message.text
        text = db.insert_users(name, surname, message.from_user.id)
        markup = klava(['Кнопка'])
        bot.send_message(message.chat.id, text, reply_markup=markup)

bot.enable_save_next_step_handlers()
bot.load_next_step_handlers()

bot.polling(none_stop=True)
