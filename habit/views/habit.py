
from rest_framework import generics
from habit.serializers.habit import HabitSerializer, HabitCreateSerializer
from habit.models import Habit


class HabitCreateView(generics.CreateAPIView):
    """Создает привычку"""
    serializer_class = HabitCreateSerializer
    queryset = Habit.objects.all()


class HabitListView(generics.ListAPIView):
    """Выводим список привычек"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()


class HabitRetrieveView(generics.RetrieveAPIView):
    """Выводит одну привычку"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()


class HabitUpdateView(generics.UpdateAPIView):
    """Обновляет привычку"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()


class HabitDestroyView(generics.DestroyAPIView):
    """Удаляет привычку"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
