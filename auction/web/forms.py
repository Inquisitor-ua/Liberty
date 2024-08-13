from .models import Zapis
from django.forms import ModelForm, TextInput, NumberInput

class ZapisInput(ModelForm):
    class Meta:
        model = Zapis

        fields = ['name', 'socset', 'age', 'rasklad', 'about']

        widgets = {'name':TextInput(attrs={
            'placeholder': 'Имя',
            'class': 'rasklad-input',
            'name': 'name'
        }),
        'socset': TextInput(attrs={
            'placeholder': 'Ваша соц.сеть: (телеграм, инстаграм)',
            'class': 'rasklad-input',
            'name': 'socset'
        }),
        'age':NumberInput(attrs={
            'placeholder': 'Возраст',
            'class': 'rasklad-input',
            'name': 'username'
        }),
        'rasklad':TextInput(attrs={
            'placeholder': 'название расклада',
            'class': 'rasklad-input',
            'name': 'rasklad'
        }),
        'about':TextInput(attrs={
            'placeholder': 'пред.история',
            'class': 'rasklad-input',
            'name': 'about'
        })
        }