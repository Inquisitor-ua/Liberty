from django.shortcuts import render
from django.http import HttpResponse
from .models import Rasklad
from .forms import ZapisInput
import telebot

TOKEN = "7291448617:AAE0-N7lM1y5zWUOfgj7lwE_JFvYVivE1VY"
# Create your views here.
def home(request):
    return render(request, "web/index.html")

def two(request):
    data = Rasklad.objects.all()
    return render(request, "web/index2.html", {'rasklads': data})

def rasklad(request):
    error = ''
    if request.method == 'POST':
        form = ZapisInput(request.POST)
        if form.is_valid():
            form.save()
            bot = telebot.TeleBot(TOKEN)
            msg = f"Имя: {form.data.get('name')}\nСоцсеть: {form.data.get('socset')}\nВозраст: {form.data.get('age')}\nРасклад: {form.data.get('rasklad')}\nОписание: {form.data.get('about')}"
            bot.send_message(892951051, msg)
        else:
            error = 'Ошибка отправки данных'
    form = ZapisInput()
    data = {'form': form, 'error': error}
    return render(request, "web/rasklad.html", data)