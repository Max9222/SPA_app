
from celery import shared_task

from habit.models import Habit
from users.services import tg_send_message
from config.settings import TELEGRAM_ID


@shared_task
def telegram_bot(**kwargs):
    """Отправка напоминания о привычке"""
    habit = Habit.objects.get(id=1)
    tg_send_message(TELEGRAM_ID, str(habit))
