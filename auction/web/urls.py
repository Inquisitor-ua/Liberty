from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name='glavnaya'),
    path("catalog/", views.two, name='catalog'),
    path("rasklad/<int:rasklad_id>", views.rasklad, name='rasklad'),
    path("rasklad/", views.rasklad, name='rasklad'),
    path("otzuvu/", views.otzuvu, name='otzuvu'),
]