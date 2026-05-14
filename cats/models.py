from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_migrate
from django.dispatch import receiver
import datetime

User = get_user_model()

CHOICES = (
    ('Gray', 'Серый'), ('Black', 'Чёрный'), ('White', 'Белый'),
    ('Ginger', 'Рыжий'), ('Mixed', 'Смешанный'),
)

class Achievement(models.Model):
    name = models.CharField(max_length=64)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self): 
        return self.name


class Cat(models.Model):
    name = models.CharField(max_length=16)
    color = models.CharField(max_length=16, choices=CHOICES)
    birth_year = models.IntegerField()
    owner = models.ForeignKey(User, related_name='cats', on_delete=models.CASCADE)
    achievements = models.ManyToManyField(Achievement, through='AchievementCat')
    views_count = models.PositiveIntegerField(default=0, verbose_name='Просмотры')
    rating_points = models.IntegerField(default=0, verbose_name='Рейтинг кота')
    likes_count = models.PositiveIntegerField(default=0, verbose_name='Лайки')

    class Meta:
        constraints = [models.UniqueConstraint(fields=['name', 'owner'], name='unique_name_owner')]

    def __str__(self): 
        return self.name
    
    def add_like(self, user):
        """Добавляет лайк от пользователя"""
        if self.owner == user:
            return False, "Нельзя лайкать своего кота"
        
        like, created = CatLike.objects.get_or_create(cat=self, user=user)
        if created:
            self.likes_count += 1
            self.rating_points += 5
            self.save()
            return True, "❤️ Лайк поставлен! +5 очков рейтинга"
        return False, "Вы уже лайкали этого кота"
    
    def remove_like(self, user):
        """Удаляет лайк"""
        try:
            like = CatLike.objects.get(cat=self, user=user)
            like.delete()
            self.likes_count -= 1
            self.rating_points -= 5
            self.save()
            return True, "🤍 Лайк убран"
        except CatLike.DoesNotExist:
            return False, "Вы не лайкали этого кота"
    
    def is_liked_by(self, user):
        """Проверяет, лайкнул ли пользователь кота"""
        if not user.is_authenticated:
            return False
        return CatLike.objects.filter(cat=self, user=user).exists()


class AchievementCat(models.Model):
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE)
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)


class CatLike(models.Model):
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cat_likes')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('cat', 'user')


class SeasonEvent(models.Model):
    SEASON_CHOICES = [
        ('winter', 'Зима'),
        ('spring', 'Весна'),
        ('summer', 'Лето'),
        ('autumn', 'Осень'),
    ]
    name = models.CharField(max_length=100, verbose_name="Название события")
    season = models.CharField(max_length=10, choices=SEASON_CHOICES, verbose_name="Сезон")
    start_date = models.DateField(verbose_name="Дата начала")
    end_date = models.DateField(verbose_name="Дата окончания")
    description = models.TextField(verbose_name="Описание", blank=True)
    bonus_points = models.IntegerField(default=10, verbose_name="Бонусные очки за участие")

    class Meta:
        verbose_name = "Сезонное событие"
        verbose_name_plural = "Сезонные события"

    def __str__(self):
        return f"{self.name} ({self.get_season_display()})"

    def is_active(self):
        today = datetime.date.today()
        return self.start_date <= today <= self.end_date


class Participation(models.Model):
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE, related_name='participations')
    event = models.ForeignKey(SeasonEvent, on_delete=models.CASCADE, related_name='participations')
    joined_at = models.DateTimeField(auto_now_add=True)
    points_earned = models.IntegerField(default=0, verbose_name="Заработанные очки")

    class Meta:
        unique_together = ('cat', 'event')

    def __str__(self):
        return f"{self.cat.name} -> {self.event.name}"


# Сигнал для автоматического создания достижений
@receiver(post_migrate)
def create_initial_achievements(sender, **kwargs):
    if sender.name == 'cats':
        achievements_list = [
            "🏆 Любитель рыбки", "🎯 Мастер охоты", "😴 Король сна",
            "💝 Самый ласковый", "🦘 Прыгун года", "🍽️ Гурман",
            "🎵 Чемпион по мурчанию", "🤝 Лучший друг", "🏠 Хранитель дома",
            "✨ Золотые лапки", "🔍 Исследователь", "📸 Звезда Instagram",
            "🥇 Олимпийский чемпион", "🎭 Дипломат", "🧠 Мудрец"
        ]
        
        for ach_name in achievements_list:
            Achievement.objects.get_or_create(name=ach_name)