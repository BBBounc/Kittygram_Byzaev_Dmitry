from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import PermissionDenied
from django.utils import timezone
from rest_framework import viewsets, permissions, status as http_status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from .models import Cat, Achievement, SeasonEvent, Participation
from .serializers import CatSerializer, AchievementSerializer, SeasonEventSerializer, ParticipationSerializer
from .forms import CatForm  # ItemForm удалён

# Permission
class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if hasattr(obj, 'owner'):
            return obj.owner == request.user
        return False


# API ViewSets
class AchievementViewSet(viewsets.ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ('name',)


class SeasonEventViewSet(viewsets.ModelViewSet):
    queryset = SeasonEvent.objects.all()
    serializer_class = SeasonEventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ('season',)
    search_fields = ('name',)
    ordering_fields = ['start_date', 'end_date', 'bonus_points', 'name', 'id']
    ordering = ['-start_date']  # Сортировка по умолчанию


class ParticipationViewSet(viewsets.ModelViewSet):
    queryset = Participation.objects.all()
    serializer_class = ParticipationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Participation.objects.filter(cat__owner=self.request.user)

    @action(detail=False, methods=['post'])
    def join_event(self, request):
        cat_id = request.data.get('cat_id')
        event_id = request.data.get('event_id')
        
        try:
            cat = Cat.objects.get(id=cat_id, owner=request.user)
            event = SeasonEvent.objects.get(id=event_id)
        except (Cat.DoesNotExist, SeasonEvent.DoesNotExist):
            return Response({'error': 'Кот или событие не найдены'}, status=http_status.HTTP_404_NOT_FOUND)
        
        if not event.is_active():
            return Response({'error': 'Событие уже не активно'}, status=http_status.HTTP_400_BAD_REQUEST)
        
        participation, created = Participation.objects.get_or_create(cat=cat, event=event)
        if created:
            participation.points_earned = event.bonus_points
            participation.save()
            # Начисляем рейтинг коту
            cat.rating_points += event.bonus_points
            cat.save()
            return Response(ParticipationSerializer(participation).data, status=http_status.HTTP_201_CREATED)
        else:
            return Response({'error': 'Кот уже участвует в этом событии'}, status=http_status.HTTP_400_BAD_REQUEST)


class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['color', 'owner']
    search_fields = ['name']
    ordering_fields = ['birth_year', 'rating_points', 'name', 'id', 'views_count', 'likes_count']
    ordering = ['-id']  # Сортировка по умолчанию

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(detail=True, methods=['get'])
    def rating_history(self, request, pk=None):
        cat = self.get_object()
        participations = cat.participations.all()
        serializer = ParticipationSerializer(participations, many=True)
        return Response(serializer.data)


# Фронтенд вьюхи
def index(request):
    active_events = [e for e in SeasonEvent.objects.all() if e.is_active()]
    top_cats = Cat.objects.order_by('-rating_points')[:5]
    return render(request, 'index.html', {
        'active_events': active_events,
        'top_cats': top_cats,
        'total_cats': Cat.objects.count()
    })


def cat_list(request):
    cats = Cat.objects.all().order_by('-rating_points')
    return render(request, 'cats/cat_list.html', {'cats': cats})


def cat_detail(request, pk):
    cat = get_object_or_404(Cat, pk=pk)
    cat.views_count += 1
    cat.save()
    events_participated = cat.participations.select_related('event').all()
    
    # Проверяем, лайкнул ли текущий пользователь этого кота
    user_liked = False
    if request.user.is_authenticated:
        user_liked = cat.is_liked_by(request.user)
    
    return render(request, 'cats/cat_detail.html', {
        'cat': cat,
        'events_participated': events_participated,
        'user_liked': user_liked,  # Передаём флаг в шаблон
    })

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


def event_list(request):
    events = SeasonEvent.objects.all()
    return render(request, 'events/event_list.html', {'events': events})


def event_detail(request, pk):
    event = get_object_or_404(SeasonEvent, pk=pk)
    participants = event.participations.select_related('cat').all()
    return render(request, 'events/event_detail.html', {
        'event': event,
        'participants': participants
    })


@login_required
def join_event(request, event_id, cat_id):
    try:
        cat = Cat.objects.get(id=cat_id, owner=request.user)
        event = SeasonEvent.objects.get(id=event_id)
    except (Cat.DoesNotExist, SeasonEvent.DoesNotExist):
        return redirect('event_list')
    
    if event.is_active():
        participation, created = Participation.objects.get_or_create(cat=cat, event=event)
        if created:
            participation.points_earned = event.bonus_points
            participation.save()
            cat.rating_points += event.bonus_points
            cat.save()
    return redirect('event_detail', pk=event_id)


@login_required
def profile(request):
    my_cats = Cat.objects.filter(owner=request.user)
    my_participations = Participation.objects.filter(cat__owner=request.user).select_related('event', 'cat')
    return render(request, 'registration/profile.html', {
        'my_cats': my_cats,
        'my_participations': my_participations
    })


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

@login_required
def like_cat(request, cat_id):
    """Лайк кота"""
    cat = get_object_or_404(Cat, id=cat_id)
    
    if request.method == 'POST':
        success, message = cat.add_like(request.user)
        if success:
            from django.contrib import messages
            messages.success(request, message)
        else:
            messages.error(request, message)
    
    return redirect('cat_detail', pk=cat_id)

@login_required
def unlike_cat(request, cat_id):
    """Убрать лайк"""
    cat = get_object_or_404(Cat, id=cat_id)
    
    if request.method == 'POST':
        success, message = cat.remove_like(request.user)
        if success:
            from django.contrib import messages
            messages.success(request, message)
        else:
            messages.error(request, message)
    
    return redirect('cat_detail', pk=cat_id)