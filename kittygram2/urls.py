from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from cats.views import CatViewSet, AchievementViewSet

router = DefaultRouter()
router.register('cats', CatViewSet)
router.register('achievements', AchievementViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('admin/', admin.site.urls),
]