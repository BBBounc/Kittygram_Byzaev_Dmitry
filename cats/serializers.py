import datetime as dt
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from .models import Cat, Achievement, CHOICES

class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = ('id', 'name')

class CatSerializer(serializers.ModelSerializer):
    # Позволяет передавать список ID достижений при POST/PATCH
    achievements = serializers.PrimaryKeyRelatedField(
        queryset=Achievement.objects.all(),
        many=True,
        required=False
    )
    color = serializers.ChoiceField(choices=CHOICES)
    age = serializers.SerializerMethodField()
    owner = serializers.PrimaryKeyRelatedField(
        read_only=True, 
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Cat
        fields = ('id', 'name', 'color', 'birth_year', 'achievements', 'owner', 'age')
        validators = [
            UniqueTogetherValidator(
                queryset=Cat.objects.all(), 
                fields=('name', 'owner'),
                message='У вас уже есть кот с таким именем!'
            )
        ]

    def get_age(self, obj):
        return dt.date.today().year - obj.birth_year

    def validate_birth_year(self, value):
        year = dt.date.today().year
        if not (year - 40 < value <= year):
            raise serializers.ValidationError('Проверьте год рождения!')
        return value

    # Этот метод отвечает за то, что мы видим в ответе (GET/POST ответ)
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # Подменяем ID ачивок на их полные данные (id и name)
        representation['achievements'] = AchievementSerializer(
            instance.achievements.all(), many=True
        ).data
        return representation