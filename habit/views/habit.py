
from rest_framework import generics
from habit.serializers.habit import HabitSerializer, HabitCreateSerializer
from habit.models import Habit
from rest_framework.permissions import IsAuthenticated, AllowAny
from habit.permissions.habit import IsOwner
from habit.paginators.habit import HabitsPagination


class HabitCreateView(generics.CreateAPIView):
    """Создает привычку"""
    serializer_class = HabitCreateSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated]


    def perform_create(self, serializer):
        new_habit = serializer.save()
        new_habit.user = self.request.user
        new_habit.save()


class HabitListView(generics.ListAPIView):
    """Выводим список привычек"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated]

    pagination_class = HabitsPagination

    def get_queryset(self):
        return Habit.objects.filter(owner=self.request.user)


class HabitRetrieveView(generics.RetrieveAPIView):
    """Выводит одну привычку"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [AllowAny]


class HabitUpdateView(generics.UpdateAPIView):
    """Обновляет привычку"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated]


class HabitDestroyView(generics.DestroyAPIView):
    """Удаляет привычку"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated]

class PublicListView(generics.ListAPIView):
    """Выводит список с флагом True = published"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.filter(published=True)
    permission_classes = [AllowAny]
    pagination_class = HabitsPagination
