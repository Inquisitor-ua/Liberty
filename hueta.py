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
    else:
        bot.send_message(message.chat.id, "твая мои не понимать")
    
bot.polling(none_stop=True)