from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from rest_framework.routers import DefaultRouter
from cats.views import *

router = DefaultRouter()
router.register('cats', CatViewSet)
router.register('items', ItemViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    
    # --- Auth ---
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/profile/', profile, name='profile'),

    # --- Frontend Главная и Списки ---
    path('', index, name='index'),
    path('items/', item_list, name='item_list'),
    path('cats/', cat_list, name='cat_list'),

    # --- Детальные страницы (счетчик просмотров работает здесь) ---
    path('items/<int:pk>/', item_detail, name='item_detail'),
    path('cats/<int:pk>/', cat_detail, name='cat_detail'),

    # --- КОТЫ: Создание, Редактирование, Удаление ---
    path('cats/add/', cat_create, name='cat_create'),
    path('cats/<int:pk>/edit/', cat_edit, name='cat_edit'),
    path('cats/<int:pk>/delete/', cat_delete, name='cat_delete'),

    # --- ВЕЩИ: Создание, Редактирование, Удаление ---
    path('items/add/', item_create, name='item_create'),
    path('items/<int:pk>/edit/', item_edit, name='item_edit'),
    path('items/<int:pk>/delete/', item_delete, name='item_delete'),
]