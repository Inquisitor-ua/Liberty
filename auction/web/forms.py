from .models import Zapis, Otzuvu
from django.forms import ModelForm, TextInput, NumberInput, HiddenInput

class OtzivInput(ModelForm):
    class Meta:
        model = Otzuvu
        
        fields = ['name', 'text', 'mark_speed', 'mark_trak', 'mark_all']
        
        widgets = {'name': TextInput(attrs={
            'class': 'rasklad-input otzuv-input',
            'name': 'name',
            'placeholder': 'Имя'
        }),
                   'text': TextInput(attrs={
            'class': 'rasklad-input',
            'name': 'text',
            'placeholder': 'Отзыв'
        }),
                   'mark_speed': HiddenInput(attrs={
            'name': 'mark_speed',
            'class': 'mark'
        }),
                   'mark_trak': HiddenInput(attrs={
            'name': 'mark_trak',
            'class': 'mark'
        }),
                   'mark_all': HiddenInput(attrs={
            'name': 'mark_all',
            'class': 'mark'
        })}

class ZapisInput(ModelForm):
    class Meta:
        model = Zapis

        fields = ['sex','name', 'socset', 'age', 'rasklad', 'about']

        widgets = {'sex': HiddenInput(attrs={
            'class': 'rasklad-input',
            'name': 'sex',
            'value': 'Мужской',
            'id': 'sex-field'
        }),
        'name':TextInput(attrs={
            'placeholder': 'Имя',
            'class': 'rasklad-input with-photo',
            'name': 'name'
        }),
        'socset': TextInput(attrs={
            'placeholder': 'Ваша соц.сеть',
            'class': 'rasklad-input',
            'name': 'socset'
        }),
        'age':NumberInput(attrs={
            'placeholder': 'Возраст',
            'class': 'rasklad-input',
            'name': 'username'
        }),
        'rasklad':TextInput(attrs={
            'placeholder': 'Название расклада',
            'class': 'rasklad-input',
            'name': 'rasklad'
        }),
        'about':TextInput(attrs={
            'placeholder': 'Пред.история',
            'class': 'rasklad-input',
            'name': 'about'
        })
        }