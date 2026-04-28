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
    # Исправил: убрал запятую в конце, чтобы поле инициализировалось правильно
    achievements = models.ManyToManyField(Achievement, through='AchievementCat')
    views_count = models.PositiveIntegerField(default=0, verbose_name='Просмотры')

    # Добавил метод расчета возраста (удобно для вывода в шаблоне)
    @property
    def age(self):
        return datetime.datetime.now().year - self.birth_year

    class Meta:
        constraints = [models.UniqueConstraint(fields=['name', 'owner'], name='unique_name_owner')]

    def __str__(self): return self.name

class AchievementCat(models.Model):
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE)
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)

class Item(models.Model):
    CATEGORY_CHOICES = [
        ('food', 'Корм'), ('clothes', 'Вещи'),
        ('toys', 'Игрушки'), ('carriers', 'Переноски'),
    ]
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField()
    color = models.CharField(max_length=30, blank=True, null=True)
    price = models.PositiveIntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='items')
    # Поле просмотров для вещей уже на месте
    views_count = models.PositiveIntegerField(default=0, verbose_name='Просмотры')
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self): return self.title