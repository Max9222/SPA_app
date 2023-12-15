
from rest_framework import generics
from habit.serializers.habit import *
from habit.models import Habit


class HabitCreateView(generics.CreateAPIView):
    """Создает привычку"""
    serializers_class = HabitCreateSerializer


class HabitListView(generics.ListAPIView):
    """Выводим список привычек"""
    serializers_class = HabitSerializer
    queryset = Habit.objects.all()


class HabitRetrieveView(generics.RetrieveAPIView):
    """Выводит одну привычку"""
    serializers_class = HabitSerializer
    queryset = Habit.objects.all()


class HabitUpdateView(generics.UpdateAPIView):
    """Обновляет привычку"""
    serializers_class = HabitSerializer
    queryset = Habit.objects.all()


class HabitDestroyView(generics.DestroyAPIView):
    """Удаляет привычку"""
    serializers_class = HabitSerializer
    queryset = Habit.objects.all()
