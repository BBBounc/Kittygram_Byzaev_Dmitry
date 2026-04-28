from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import PermissionDenied
from rest_framework import viewsets, permissions

from .models import Cat, Item, Achievement
from .serializers import CatSerializer, ItemSerializer, AchievementSerializer
from .forms import CatForm, ItemForm

# --- API ViewSets ---
class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        owner = getattr(obj, 'owner', getattr(obj, 'author', None))
        return owner == request.user

class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    def perform_create(self, serializer): 
        serializer.save(owner=self.request.user)

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    def perform_create(self, serializer): 
        serializer.save(author=self.request.user)

# --- HTML Frontend (Главная и Списки) ---

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

# --- Детальные страницы с просмотрами ---

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

# --- КОТЫ (Создание, Редактирование, Удаление) ---

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

# --- ВЕЩИ (Создание, Редактирование, Удаление) ---

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

# --- Профиль и Регистрация ---

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