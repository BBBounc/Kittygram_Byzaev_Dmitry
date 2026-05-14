from django import forms
from .models import Cat

class CatForm(forms.ModelForm):
    class Meta:
        model = Cat
        fields = ['name', 'color', 'birth_year', 'achievements']
        labels = {
            'name': 'Имя котика',
            'color': 'Цвет',
            'birth_year': 'Год рождения',
            'achievements': 'Достижения',
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full p-3 rounded-xl border border-gray-200 outline-none focus:border-indigo-500',
                'placeholder': 'Например, Барсик'
            }),
            'color': forms.Select(attrs={
                'class': 'w-full p-3 rounded-xl border border-gray-200 outline-none focus:border-indigo-500'
            }),
            'birth_year': forms.NumberInput(attrs={
                'class': 'w-full p-3 rounded-xl border border-gray-200 outline-none focus:border-indigo-500',
                'min': 1990,
                'max': 2026
            }),
            'achievements': forms.SelectMultiple(attrs={
                'class': 'w-full p-3 rounded-xl border border-gray-200 outline-none min-h-[120px]',
                'help_text': 'Зажмите Ctrl для выбора нескольких вариантов'
            }),
        }