from django.db import models

# Create your models here.
class Rasklad(models.Model):
    name = models.CharField('Название раскладов', max_length= 100)
    voprosi = models.CharField('Вопросы расклада', max_length=1024)
    price = models.IntegerField("Цена")
    description = models.TextField('Описание')
    date = models.DateField('Дата публикации')
    def __str__(self):
        return self.name
    

class Zapis(models.Model):
    name = models.CharField('Имя клиента', max_length=64)
    socset = models.CharField('Название соцсети', max_length=128)
    rasklad = models.CharField('Название расклада', max_length=128)
    age = models.IntegerField('Возраст')
    about = models.TextField('Описание расклада')