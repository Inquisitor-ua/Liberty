import telebot
import config

TOKEN = config.BOT_TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start", "home"])
def hello(message):
    bot.reply_to(message, "Привет, малиш")

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
bot.polling(none_stop=True)