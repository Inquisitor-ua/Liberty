from django.shortcuts import render
from django.http import HttpResponse
from .models import Rasklad
from .forms import ZapisInput
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
            
        else:
            error = 'Ошибка отправки данных'
    form = ZapisInput()
    data = {'form': form, 'error': error}
    return render(request, "web/rasklad.html", data)