from django.core.management import BaseCommand

from habit.models import Habit
from users.services import MyBot, tg_send_message


class Command(BaseCommand):

    def handle(self, *args, **options):
        """Отправка напоминания о привычке"""
        my_bot = MyBot()
        habit = Habit.objects.get(id=1)
        my_bot.send_massage(habit)
