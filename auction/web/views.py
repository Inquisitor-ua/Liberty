from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, "web/index.html")

def two(request):
    return render(request, "web/index2.html")