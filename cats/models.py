from django.contrib.auth import get_user_model
from django.db import models
import datetime

User = get_user_model()

CHOICES = (
    ('Gray', 'Серый'), ('Black', 'Чёрный'), ('White', 'Белый'),
    ('Ginger', 'Рыжий'), ('Mixed', 'Смешанный'),
)

class Achievement(models.Model):
    name = models.CharField(max_length=64)
    def __str__(self): return self.name

class Cat(models.Model):
    name = models.CharField(max_length=16)
    color = models.CharField(max_length=16, choices=CHOICES)
    birth_year = models.IntegerField()
    owner = models.ForeignKey(User, related_name='cats', on_delete=models.CASCADE)
    achievements = models.ManyToManyField(Achievement, through='AchievementCat')
    views_count = models.PositiveIntegerField(default=0, verbose_name='Просмотры')

    class Meta:
        constraints = [models.UniqueConstraint(fields=['name', 'owner'], name='unique_name_owner')]

    def __str__(self): return self.name

class AchievementCat(models.Model):
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE)
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)

# НОВАЯ МОДЕЛЬ ДЛЯ КАТЕГОРИЙ
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название")
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
    def __str__(self): return self.name

class Item(models.Model):
    STATUS_CHOICES = [
        ('available', 'Доступно'),
        ('reserved', 'Забронировано'),
        ('given', 'Передано'),
    ]

    title = models.CharField(max_length=100)
    # Заменили текстовое поле на связь
    category = models.ForeignKey(
        Category, 
        on_delete=models.SET_NULL, 
        null=True, 
        related_name='items',
        verbose_name="Категория"
    )
    description = models.TextField()
    color = models.CharField(max_length=30, blank=True, null=True)
    price = models.PositiveIntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='items')
    views_count = models.PositiveIntegerField(default=0, verbose_name='Просмотры')
    pub_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')
    reserved_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, related_name='booked_items'
    )

    def __str__(self): return self.title