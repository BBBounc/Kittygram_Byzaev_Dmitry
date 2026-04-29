from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import PermissionDenied
from rest_framework import viewsets, permissions, status as http_status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from .models import Cat, Item, Achievement, Category
from .serializers import CatSerializer, ItemSerializer, AchievementSerializer, CategorySerializer
from .forms import CatForm, ItemForm

# Разрешения кастом
class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        owner = getattr(obj, 'owner', getattr(obj, 'author', None))
        return owner == request.user

# вьюшки апишки

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ('name',)
    search_fields = ('name',)

class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ('color', 'owner')
    search_fields = ('name',)
    ordering_fields = ('birth_year',)
    
    def perform_create(self, serializer): 
        serializer.save(owner=self.request.user)

class AchievementViewSet(viewsets.ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer
    # Достижения могут смотреть все, а редактировать только админ или авторизованный
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ('name',)

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ('category__name', 'status', 'color') # Фильтр по имени категории
    search_fields = ('title', 'description')
    ordering_fields = ('price', 'pub_date')

    def perform_create(self, serializer): 
        serializer.save(author=self.request.user)

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def reserve(self, request, pk=None):
        item = self.get_object()
        if item.status != 'available':
            return Response({'error': 'Вещь недоступна'}, status=http_status.HTTP_400_BAD_REQUEST)
        if item.author == request.user:
            return Response({'error': 'Свою вещь бронировать нельзя'}, status=http_status.HTTP_400_BAD_REQUEST)
        item.status = 'reserved'
        item.reserved_by = request.user
        item.save()
        return Response({'message': 'Успешно забронировано'})

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def cancel(self, request, pk=None):
        item = self.get_object()
        item.status = 'available'
        item.reserved_by = None
        item.save()
        return Response({'message': 'Бронь отменена'})

    @action(detail=True, methods=['post'], permission_classes=[IsOwnerOrReadOnly])
    def confirm(self, request, pk=None):
        item = self.get_object()
        if item.status != 'reserved':
            return Response({'error': 'Вещь не была забронирована'}, status=http_status.HTTP_400_BAD_REQUEST)
        item.status = 'given'
        item.save()
        return Response({'message': 'Передача подтверждена'})

# Логика перехода на страницы

def index(request):
    latest_items = Item.objects.all().order_by('-pub_date')[:3]
    total_cats = Cat.objects.count()
    return render(request, 'index.html', {'latest_items': latest_items, 'total_cats': total_cats})

def item_list(request):
    items = Item.objects.all().order_by('-pub_date')
    return render(request, 'items_list.html', {'items': items})

def cat_list(request):
    cats = Cat.objects.all()
    return render(request, 'cats/cat_list.html', {'cats': cats})

def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    item.views_count += 1
    item.save()
    return render(request, 'items/item_detail.html', {'item': item})

def cat_detail(request, pk):
    cat = get_object_or_404(Cat, pk=pk)
    cat.views_count += 1
    cat.save()
    return render(request, 'cats/cat_detail.html', {'cat': cat})

# Логика CRUD для котиииииков

@login_required
def cat_create(request):
    form = CatForm(request.POST or None)
    if form.is_valid():
        cat = form.save(commit=False)
        cat.owner = request.user
        cat.save()
        form.save_m2m()
        return redirect('cat_list')
    return render(request, 'form.html', {'form': form, 'title': 'Добавить котика'})

@login_required
def cat_edit(request, pk):
    cat = get_object_or_404(Cat, pk=pk)
    if cat.owner != request.user:
        raise PermissionDenied
    form = CatForm(request.POST or None, instance=cat)
    if form.is_valid():
        form.save()
        return redirect('cat_detail', pk=pk)
    return render(request, 'form.html', {'form': form, 'title': 'Редактировать котика'})

@login_required
def cat_delete(request, pk):
    cat = get_object_or_404(Cat, pk=pk)
    if cat.owner != request.user:
        raise PermissionDenied
    if request.method == 'POST':
        cat.delete()
        return redirect('cat_list')
    return render(request, 'confirm_delete.html', {'obj': cat})

# Логика CRUD на объявления

@login_required
def item_create(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        item = form.save(commit=False)
        item.author = request.user
        item.save()
        return redirect('item_list')
    return render(request, 'form.html', {'form': form, 'title': 'Новое объявление'})

@login_required
def item_edit(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if item.author != request.user:
        raise PermissionDenied
    form = ItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('item_detail', pk=pk)
    return render(request, 'form.html', {'form': form, 'title': 'Редактировать объявление'})

@login_required
def item_delete(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if item.author != request.user:
        raise PermissionDenied
    if request.method == 'POST':
        item.delete()
        return redirect('item_list')
    return render(request, 'confirm_delete.html', {'obj': item})

# Логика взаимодействия с объявлениями

@login_required
def item_reserve(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if item.status == 'available' and item.author != request.user:
        item.status = 'reserved'
        item.reserved_by = request.user
        item.save()
    return redirect('item_detail', pk=pk)

@login_required
def item_cancel_reserve(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if item.reserved_by == request.user or item.author == request.user:
        item.status = 'available'
        item.reserved_by = None
        item.save()
    return redirect('item_detail', pk=pk)

@login_required
def item_confirm_given(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if item.author == request.user and item.status == 'reserved':
        item.status = 'given'
        item.save()
    return redirect('item_detail', pk=pk)

# Вьюшки на регистрацию и переход на профиль 

@login_required
def profile(request):
    my_cats = Cat.objects.filter(owner=request.user)
    my_items = Item.objects.filter(author=request.user)
    return render(request, 'registration/profile.html', {'my_cats': my_cats, 'my_items': my_items})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})