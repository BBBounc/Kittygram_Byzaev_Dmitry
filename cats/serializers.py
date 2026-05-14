import datetime as dt
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from .models import Cat, Achievement, SeasonEvent, Participation


class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = ('id', 'name')


class SeasonEventSerializer(serializers.ModelSerializer):
    is_active = serializers.BooleanField(read_only=True)

    class Meta:
        model = SeasonEvent
        fields = ('id', 'name', 'season', 'start_date', 'end_date', 'description', 'bonus_points', 'is_active')


class ParticipationSerializer(serializers.ModelSerializer):
    cat_name = serializers.ReadOnlyField(source='cat.name')
    event_name = serializers.ReadOnlyField(source='event.name')
    
    class Meta:
        model = Participation
        fields = ('id', 'cat', 'cat_name', 'event', 'event_name', 'joined_at', 'points_earned')
        read_only_fields = ('joined_at', 'points_earned')


class CatSerializer(serializers.ModelSerializer):
    achievements = serializers.PrimaryKeyRelatedField(
        queryset=Achievement.objects.all(), many=True, required=False
    )
    age = serializers.SerializerMethodField()
    owner = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = Cat
        # Убрали total_rating, оставили rating_points
        fields = ('id', 'name', 'color', 'birth_year', 'achievements', 'owner', 'age', 'views_count', 'rating_points', 'likes_count')
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