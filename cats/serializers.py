import datetime as dt
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from .models import Cat, Achievement, CHOICES, Item

class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = ('id', 'name')

class ItemSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)
    likes_count = serializers.IntegerField(source='likes.count', read_only=True)

    class Meta:
        model = Item
        fields = '__all__'

    def validate(self, data):
        user = self.context['request'].user
        if self.context['request'].method == 'POST':
            if Item.objects.filter(author=user).count() >= 5:
                raise serializers.ValidationError('Лимит: не более 5 вещей на пользователя!')
        return data

class CatSerializer(serializers.ModelSerializer):
    achievements = serializers.PrimaryKeyRelatedField(
        queryset=Achievement.objects.all(), many=True, required=False
    )
    age = serializers.SerializerMethodField()
    owner = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = Cat
        fields = ('id', 'name', 'color', 'birth_year', 'achievements', 'owner', 'age')
        validators = [
            UniqueTogetherValidator(
                queryset=Cat.objects.all(), fields=('name', 'owner'),
                message='У вас уже есть кот с таким именем!'
            )
        ]

    def get_age(self, obj):
        return dt.date.today().year - obj.birth_year

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['achievements'] = AchievementSerializer(
            instance.achievements.all(), many=True
        ).data
        return representation