from rest_framework import viewsets
from .models import Achievement, Cat
from .serializers import AchievementSerializer, CatSerializer

class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer

    def perform_create(self, serializer):
        # Принудительно сохраняем кота за тем, кто сделал запрос
        serializer.save(owner=self.request.user)

class AchievementViewSet(viewsets.ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer