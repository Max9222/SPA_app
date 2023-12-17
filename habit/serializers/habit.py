from rest_framework import serializers
from habit.models import Habit
from habit.validators.habit import IsNiceValidator, NiceValidator, TimeValidator, PeriodValidator


class PleasureHabitSerializer(serializers.ModelSerializer):
    """Полезная привычка"""
    class Meta:
        model = Habit
        fields = ('owner', 'place', 'time_start', 'action', 'period', 'time_period', 'published', 'pleasant_habit',)


class HabitSerializer(serializers.ModelSerializer):
    """Привычка"""
    pleasure_habit = PleasureHabitSerializer(source='habit', many=True)

    class Meta:
        model = Habit
        fields = '__all__'


class HabitCreateSerializer(serializers.ModelSerializer):
    """Создание привычки"""
    class Meta:
        model = Habit
        fields = ('id', 'owner', 'place', 'time_start', 'action', 'nice', 'period', 'reward', 'time_period',
                  'published', 'pleasant_habit',)
        validators = [NiceValidator(fields),
                      IsNiceValidator(field='pleasant_habit'),
                      TimeValidator(field='time_period'),
                      PeriodValidator(field='period')]
