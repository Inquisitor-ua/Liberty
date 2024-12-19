from .models import Zapis, Otzuvu
from django.forms import ModelForm, TextInput, NumberInput, HiddenInput

class OtzivInput(ModelForm):
    class Meta:
        model = Otzuvu
        
        fields = ['name', 'text', 'mark']
        
        widgets = {'name': TextInput(attrs={
            'class': ...,
            'name': 'name',
            'placeholder': 'Имя'
        }),
                   'text': TextInput(attrs={
            'class': ...,
            'name': 'text',
            'placeholder': 'Отзыв'
        }),
                   'mark': HiddenInput(attrs={
            'class': ...,
            'name': 'mark',
            'id': 'mark'
        }),}

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