from django.contrib import admin
from .models import Rasklad, Zapis, Otzuvu

# Register your models here.
admin.site.register(Rasklad)
admin.site.register(Zapis)
admin.site.register(Otzuvu)