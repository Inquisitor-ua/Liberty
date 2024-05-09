import telebot

TOKEN = "6867993743:AAHBg7sQvBj2Va8ZSUZ3YDZkKg8Mkrdj9ac"

bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=["start", "home"])
def hello(message):
    bot.reply_to(message, "Привет, малиш")

@bot.message_handler(content_types=["text"])
def message(message):
    bot.send_message(message.chat.id, "твая мои не понимать")
bot.polling(none_stop=True)