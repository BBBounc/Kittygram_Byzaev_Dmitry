from django import forms
from .models import Cat, Item, Achievement

class CatForm(forms.ModelForm):
    class Meta:
        model = Cat
        # Мы исключаем 'owner' и 'views_count', так как они заполняются автоматически
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

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        # Исключаем 'author', 'views_count' и 'pub_date'
        fields = ['title', 'category', 'description', 'color', 'price']
        labels = {
            'title': 'Название объявления',
            'category': 'Категория',
            'description': 'Описание',
            'color': 'Цвет (если применимо)',
            'price': 'Цена (₽)',
        }
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full p-3 rounded-xl border border-gray-200 outline-none focus:border-indigo-500',
                'placeholder': 'Например, Кошачья мята'
            }),
            'category': forms.Select(attrs={
                'class': 'w-full p-3 rounded-xl border border-gray-200 outline-none focus:border-indigo-500'
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full p-3 rounded-xl border border-gray-200 outline-none focus:border-indigo-500',
                'rows': 4,
                'placeholder': 'Опишите состояние и детали...'
            }),
            'color': forms.TextInput(attrs={
                'class': 'w-full p-3 rounded-xl border border-gray-200 outline-none focus:border-indigo-500',
                'placeholder': 'Например, синий'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'w-full p-3 rounded-xl border border-gray-200 outline-none focus:border-indigo-500',
                'min': 0
            }),
        }