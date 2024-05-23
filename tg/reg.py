import telebot
import tg.config as config
import time
import pyautogui as pg
from telebot import types
import tg.pgpg as control
import os
import webbrowser as wb
from bs4 import BeautifulSoup
import requests

TOKEN = config.BOT_TOKEN

bot = telebot.TeleBot(TOKEN)



@bot.message_handler(commands=["start", "home"])
def hello(message):
    bot.reply_to(message, "Зарегайся", reply_markup=markup)
    
markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
