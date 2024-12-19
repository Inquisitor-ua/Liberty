from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Rasklad, Otzuvu
from .forms import ZapisInput
import telebot

TOKEN = "7291448617:AAE0-N7lM1y5zWUOfgj7lwE_JFvYVivE1VY"
# Create your views here.
def home(request):
    return render(request, "web/index.html")

def two(request):
    data = Rasklad.objects.all()
    return render(request, "web/catalog.html", {'rasklads': data})

def rasklad(request):
    error = ''
    if request.method == 'POST':
        form = ZapisInput(request.POST)
        if form.is_valid():
            form.save()
            bot = telebot.TeleBot(TOKEN)
            msg = f"Имя: {form.data.get('name')}\nСоцсеть: {form.data.get('socset')}\nВозраст: {form.data.get('age')}\nРасклад: {form.data.get('rasklad')}\nОписание: {form.data.get('about')}"
            bot.send_message(892951051, msg) #892951051
            return redirect('rasklad')
        else:
            form = ZapisInput()
            error = 'Ошибка отправки данных'
    form = ZapisInput()
    data = {'form': form, 'error': error}
    return render(request, "web/rasklad.html", data)

def otzuvu(request):
    data = Otzuvu.objects.all()
    return render(request, "web/otzuvu.html", {'otzuvu': data})
