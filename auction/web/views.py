from django.shortcuts import render, redirect, get_object_or_404
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

def rasklad(request, rasklad_id = 0):
    error = ''
    if rasklad_id == 0:
        vibor = 'Самый популярный расклад:'
        rasklad = get_object_or_404(Rasklad, name='Что он думает обо мне?')
    else:
        vibor = 'Вы выбрали расклад:'
        rasklad = get_object_or_404(Rasklad, id=rasklad_id)
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
    data = {'form': form, 'error': error, 'rasklad': rasklad, 'vibor': vibor}
    return render(request, "web/rasklad.html", data)

def otzuvu(request):
    data = Otzuvu.objects.all()
    return render(request, "web/otzuvu.html", {'otzuvu': data})
