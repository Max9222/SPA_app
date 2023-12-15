from django.db import models

from config import settings

NULLABLE = {'null': True, 'blank': True}


class Habit(models.Model):
    CHOICES = [
        ('DAILY', 'каждый день'),
        ('WEEKLY', 'раз в неделю'),
    ]
    name = models.CharField(max_length=150, unique=True, verbose_name='Название привычки')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Создатель привычки')
    place = models.CharField(max_length=150, verbose_name='Место выполнения привычки')
    time_start = models.TimeField(verbose_name='Время начала', **NULLABLE)
    action = models.TextField(verbose_name='Действие привычки')
    nice = models.BooleanField(verbose_name='Признак приятной привычки')
    pleasant_habit = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='Приятная привычка', **NULLABLE)
    period = models.CharField(max_length=50, choices=CHOICES, default='DAILY', verbose_name='Периодичность')
    reward = models.TextField(verbose_name='Вознаграждение', **NULLABLE)
    time_period = models.PositiveIntegerField(verbose_name='Время на выполнение')
    published = models.BooleanField(verbose_name='Признак публичности', default=False)

    def __str__(self):
        return f"{self.action} нравится {self.owner}"

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
