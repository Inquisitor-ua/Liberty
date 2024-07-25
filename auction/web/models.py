from django.db import models

# Create your models here.
class Deti(models.Model):
    name = models.CharField('Имя фамилиия', max_length=64)
    age = models.IntegerField('Возраст')
    sex = models.CharField("Пол", max_length=16)
    price = models.FloatField("Цена")
    description = models.TextField('Описание')
    photo = models.ImageField('Фото')
    date = models.DateField('Дата публикации')
    def __str__(self):
        return self.name