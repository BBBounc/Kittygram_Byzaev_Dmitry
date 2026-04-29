from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from rest_framework.routers import DefaultRouter
from cats.views import *

router = DefaultRouter()
router.register('cats', CatViewSet)
router.register('items', ItemViewSet)
router.register('categories', CategoryViewSet)      # Теперь 404 пропадет
router.register('achievements', AchievementViewSet)

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

    # Фронт списки и главная страница
    path('', index, name='index'),
    path('items/', item_list, name='item_list'),
    path('cats/', cat_list, name='cat_list'),

    # Детальные страницы
    path('items/<int:pk>/', item_detail, name='item_detail'),
    path('cats/<int:pk>/', cat_detail, name='cat_detail'),

    # Коты CRUD
    path('cats/add/', cat_create, name='cat_create'),
    path('cats/<int:pk>/edit/', cat_edit, name='cat_edit'),
    path('cats/<int:pk>/delete/', cat_delete, name='cat_delete'),

    # Объекты CRUD 
    path('items/add/', item_create, name='item_create'),
    path('items/<int:pk>/edit/', item_edit, name='item_edit'),
    path('items/<int:pk>/delete/', item_delete, name='item_delete'),

    path('items/<int:pk>/reserve/', item_reserve, name='item_reserve_web'),
    path('items/<int:pk>/cancel/', item_cancel_reserve, name='item_cancel_web'),
    path('items/<int:pk>/confirm/', item_confirm_given, name='item_confirm_web'),
]