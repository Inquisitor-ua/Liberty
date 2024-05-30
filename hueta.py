import telebot
import tg.config as config
import time
import pyautogui as pg
from telebot import types
import os
import webbrowser as wb
from bs4 import BeautifulSoup
import requests
def pesni():
    url = "https://www.shazam.com/charts/top-200/ukraine"
    response = requests.get(url)
    html = BeautifulSoup(response.text,"lxml")
    pesni = html.find_all('div', class_='SongItem-module_card__p7LL-')
    for pesnya in pesni:
        name = pesnya.find("span" , class_ = "Text-module_text-black__mkuUo Text-module_fontFamily__cQFwR SongItem-module_ellipisLink__DsCMc Text-post-module_size-base__o144k Text-module_fontWeightBold__4NHce").text
        aftor = pesnya.find("span" , class_ = "Text-module_text-gray-900__Qcj0F Text-module_fontFamily__cQFwR SongItem-module_ellipisLink__DsCMc Text-post-module_size-base__o144k Text-module_fontWeightNormal__kB6Wg").text
        yield name, aftor


TOKEN = config.BOT_TOKEN

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start", "home"])
def hello(message):
    bot.reply_to(message, "Привет, малиш", reply_markup=markup)

@bot.message_handler(content_types=["text"])
def message(message):
    if message.text.lower() == 'запусти майнкрафт':
        bot.send_message(message.chat.id, "еще че, пшлнх")
        # control.main()
        os.startfile(r"C:\Users\evgen\OneDrive\Рабочий стол\TLauncher")

    elif message.text.lower() == "открой тг":
        bot.send_message(message.chat.id, "ладно")
        #control.telega()
        os.startfile(r"C:\Users\evgen\OneDrive\Рабочий стол\Telegram Desktop")

    elif message.text.lower() == "скинь песни":
        bot.send_message(message.chat.id, "минуточку")
        ans = ''
        number = 1
        num = 1
        for name, aftor in pesni():
            ans += f"{number}. Название: {name}, автор: {aftor}\n\n"
            if num % 20 == 0:
                num = 0
                bot.send_message(message.chat.id, ans)
                ans = ''
            number += 1
            num += 1

    elif message.text.lower() == "спой песню":
        bot.send_message(message.chat.id, "будет сделано", reply_markup=inline_markup)

    elif message.text.lower() == "иди в будку":
        bot.send_message(message.chat.id, "слушаюсь и повинуюсь")
        pg.alert(text = 'Я в будке', title = 'Будка', button = 'Сидеть')
    
    else:
        bot.send_message(message.chat.id, "не понимаю брат")
        

@bot.callback_query_handler(func=lambda call: True)
def brat(call):
    if call.data == "ya ronyau":
        bot.answer_callback_query(call.id, "я роняю запад у")
        bot.send_message(call.from_user.id, "Я роняю Запад, у! Я роняю Запад, эй! Я роняю Запад (esketit!)\nЯ роняю Запад, эй! Я роняю Запад, у! Я роняю запад, а! На моем х*е вся индустрия США, яу!\nЯ роняю Запад — это правда. Я е**л жену Обамы. Мне ***ала дочка Трампа, США в нокаут, у!\nДелаю то, что я хочу, *ончил прямо ей в *изду. Ты сосал мне, если ты касался ее губ.\nСнова **ахнул этих двух, мне не нужен друг вокруг. Они пишут в Instagram'е, просят **ахнуть своих сук.\nЯ тебя не знаю, но ты знаешь про меня. Я не видел долб**бов хуже, чем мои учителя.")
        wb.open("https://www.youtube.com/watch?v=ZGEoqPpJQLE")
    elif call.data == "rot mochi":
        bot.answer_callback_query(call.id, " нассы мне полний рот мочи")
        bot.send_message(call.from_user.id, "Плюнь мне в жопу\nПоцелуй меня в очко\nУкуси мой клитор\nИ насри мне на грудь\nНаспускай на лицо молочко\nИ воткни в анус мне что-нибудь\nмне полный рот мочи\nИ на спину мне надрочи\nЗатуши мне бычок в сосок\nИ выдерни со своего яйца волосок\nА ты *би меня, *би меня опять\nЗасунь мне пальцы в рот\nИ я начну как конь стонать\nА ты засри всю мою комнату в понос\nИ я усядусь мокрой писькой на твой нос\nРастопи одну лишь меня\nПрикоснешься рукой к моим нежным губам\nИ я крикну постой ты посмотришь в глаза\nИ увидишь любовь я отвечу тебе")
    elif call.data == "atomne":
        bot.answer_callback_query(call.id, "я запускаю в небо свое")
        bot.send_message(call.from_user.id, "Я запускаю у неба сває АТАМНЕ АРУЖИЄ\nУваґа люди тікай бо зібʼє\nЗУБАЖИННЯ НАКРИВАЄ ВСЕ\n(0-0-0-о-о-о-0)\nЗУБАЖИННЯ ЙДЕ\n(A-a-a-a-a-a)\nЗУБАЖИЄ ВСЕ\nГаз ґаз нафтаґаз\nЗа це люблю Данбас\nҐоспади памажи - всіх зубажи\nЯ як стаяла, я буду стаять\nА ти не можеш президентам абрать, давлю на\nґаз\nГаз ґаз ґаз\nЯ хочу ґаз!\nҐаз ґаз ґаз\nЯ хочу ґаз!\nГаз - ґаз - ґаз - ґаз - ґаз - ґаз\nЯ ЗАПУСКАЮ У НЕБА СВАЄ АТАМНЕ АРУЖИЄ\nУваґа люди тікай бо зібʼє\nЗУБАЖИННЯ НАКРИВАЄ ВСЕ\n(0-0-0-0-0-0-0)")
    elif call.data == "taxi":
        bot.answer_callback_query(call.id, "зеленоглазое такси ооо")
        bot.send_message(call.from_user.id, "Вот и осталось\nЛишь снять усталость\nИ этот вечер\nМне душу лечит\nО-о-о! Зеленоглазое такси\nО-о-о! Притормози, притормози\nО-о-о! И отвези меня туда\nО-о-о! Где будут рады мне всегда\nВсегда!\nТам и не спросят\nГде меня носит\nТам я-то знаю\nВсё понимают\nО-о-о! Зеленоглазое такси\nО-о-о! Притормози, притормози\nО-о-о! И отвези меня туда\nО-о-о! Где будут рады мне всегда\nВсегда!")
    elif call.data == "chorni":
        bot.answer_callback_query(call.id, "чорные глазаааааа")
        bot.send_message(call.from_user.id, "Белый снег сияет светом, черные глаза\nОсень обернется летом, черные глаза\nОколдован я тобою, черные глаза\nОслепили меня глазки, черные глаза\nЧерные глаза - вспоминаю, умираю\nЧерные глаза, я только о тебе мечтаю\nЧерные глаза - самые прекрасные!\nЧерные глаза, черные глаза, черные глаза\nЧерные глаза - вспоминаю, умираю\nЧерные глаза, я только о тебе мечтаю\nЧерные глаза - самые прекрасные!\nЧерные глаза, черные глаза, черные глаза\nЧерные глаза все помнят, - как любили мы\nСердцем чувствую я это: как любишь меня ты\nТак любить никто не сможет черные глаза\nСамые прекрасные, черные глаза\nЧерные глаза - вспоминаю, умираю\nЧерные глаза, я только о тебе мечтаю\nЧерные глаза - самые прекрасные!\nЧерные глаза, черные глаза, черные глаза")
    elif call.data == "ckazki":
        bot.answer_callback_query(call.id, "восточные сказкиииии")
        bot.send_message(call.from_user.id, "Восточные сказки,\nЗачем ты мне строишь глазки,\nМанишь, дурманишь,\nЗовёшь пойти с тобой.\nЭй, девушка-красавица,\nТы мне улыбаешься,\nЯ тебя уже люблю,\nВсё, что хочешь подарю.\nМне подарков не дари,\nЖарких слов не говори,\nИ в любви мне не клянись,\nА сначала ты женись.\nВосточные сказки,\nЗачем ты мне строишь глазки,\nМанишь, дурманишь,\nЗовёшь пойти с тобой.\nВосточные сказки,\nА может, расскажешь мне\nКакая, такая\nВосточная любовь?\nДевушка-красавица,\nТы мне очень нравишься,\nУ меня есть три жены,\nА четвёртой будешь ты.\nУважаемый, уже\nУ меня есть пять мужей,\nЯ их всех люблю, а ты,\nЕсли хочешь, будь шестым.\nВосточные сказки,\nЗачем ты мне строишь глазки,\nМанишь, дурманишь,\nЗовёшь пойти с тобой.\nВосточные сказки,\nА может, расскажешь мне\nКакая, такая\nВосточная любовь?\nТакая восточная любовь.\nТакая восточная любовь.")


markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
item1 = types.KeyboardButton("запусти майнкрафт")
item5 = types.KeyboardButton("скинь песни")
item2 = types.KeyboardButton("открой тг")
item3 = types.KeyboardButton("спой песню")
item4 = types.KeyboardButton("иди в будку")

markup.add(item1, item2, item3, item4,  item5)

inline_markup = types.InlineKeyboardMarkup(row_width=2)
inl_item1 = types.InlineKeyboardButton(text="я роняю запад",callback_data="ya ronyau")
inl_item2 = types.InlineKeyboardButton(text="нассы мне полний рот мочи",callback_data="rot mochi")
inl_item3 = types.InlineKeyboardButton(text="я запускаю атомне",callback_data="atomne")
inl_item4 = types.InlineKeyboardButton(text="зеленоглазое такси",callback_data="taxi")
inl_item5 = types.InlineKeyboardButton(text="чорные глаза",callback_data="chorni")
inl_item6 = types.InlineKeyboardButton(text="восточные сказки",callback_data="ckazki")
inline_markup.add(inl_item1,inl_item2,inl_item3,inl_item4,inl_item5,inl_item6)


bot.polling(none_stop=True)