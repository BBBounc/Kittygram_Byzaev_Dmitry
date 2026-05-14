from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from rest_framework.routers import DefaultRouter
from cats.views import *

router = DefaultRouter()
router.register('cats', CatViewSet)
router.register('achievements', AchievementViewSet)
router.register('events', SeasonEventViewSet)
router.register('participations', ParticipationViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),

    # Аутентификация
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/profile/', profile, name='profile'),

    # Главная и списки
    path('', index, name='index'),
    path('cats/', cat_list, name='cat_list'),
    path('events/', event_list, name='event_list'),

    # Детальные страницы
    path('cats/<int:pk>/', cat_detail, name='cat_detail'),
    path('events/<int:pk>/', event_detail, name='event_detail'),

    # CRUD котов
    path('cats/add/', cat_create, name='cat_create'),
    path('cats/<int:pk>/edit/', cat_edit, name='cat_edit'),
    path('cats/<int:pk>/delete/', cat_delete, name='cat_delete'),

    # Участие в событии
    path('events/<int:event_id>/join/<int:cat_id>/', join_event, name='join_event'),
    
    # Лайки
    path('cats/<int:cat_id>/like/', like_cat, name='like_cat'),
    path('cats/<int:cat_id>/unlike/', unlike_cat, name='unlike_cat'),
]