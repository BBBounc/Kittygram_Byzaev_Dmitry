import datetime as dt
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from .models import Cat, Achievement, Item, Category

class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = ('id', 'name')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')

class ItemSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)
    category = serializers.SlugRelatedField(
        slug_field='name', 
        queryset=Category.objects.all()
    )
    reserved_by_username = serializers.SlugRelatedField(
        source='reserved_by', slug_field='username', read_only=True
    )

    class Meta:
        model = Item
        fields = (
            'id', 'title', 'category', 'description', 'color', 'price', 
            'author', 'status', 'reserved_by_username', 'views_count', 'pub_date'
        )
        read_only_fields = ('status', 'reserved_by', 'views_count', 'author')

    def validate(self, data):
            request = self.context.get('request')
            if request and request.method == 'POST':
                # Считаем только те вещи автора, которые имеют статус 'available'
                active_items_count = Item.objects.filter(
                    author=request.user, 
                    status='available'
                ).count()
                
                if active_items_count >= 5:
                    raise serializers.ValidationError('Лимит: не более 5 активных объявлений на пользователя!')
            return data

class CatSerializer(serializers.ModelSerializer):
    achievements = serializers.PrimaryKeyRelatedField(
        queryset=Achievement.objects.all(), many=True, required=False
    )
    age = serializers.SerializerMethodField()
    owner = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = Cat
        fields = ('id', 'name', 'color', 'birth_year', 'achievements', 'owner', 'age', 'views_count')
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