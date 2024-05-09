import telebot
import config
from telebot import types

TOKEN = config.BOT_TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start", "home"])
def hello(message):
    bot.reply_to(message, "Привет, малиш", reply_markup=markup)

@bot.message_handler(content_types=["text"])
def message(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, "И тебе привет, дружище!")
    elif message.text.lower() == "помоги брат":
        bot.send_message(message.chat.id, "чем?")
    elif message.text.lower() == "совет":
        bot.send_message(message.chat.id, "каким")
    elif message.text.lower() == "кто я брат?":
        bot.send_message(message.chat.id, "ты брат")
    else:
        bot.send_message(message.chat.id, "не понимаю брат")
         
markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
item1 = types.KeyboardButton("Привет")
item2 = types.KeyboardButton("Помоги брат")
item3 = types.KeyboardButton("Совет")
item4 = types.KeyboardButton("Кто я брат?")
markup.add(item1, item2, item3, item4)

bot.polling(none_stop=True)