from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from habit.models import Habit
from users.models import User
import datetime

class HabitTestCase(APITestCase):

    def setUp(self) -> None:
        """Тест User"""
        self.user = User.objects.create_user(
            username='admin',
            password='admin'

        )
        '''Аутентификация пользователя'''
        self.client.force_authenticate(user=self.user)

        '''Создается тестовая привычка'''
        self.habit = Habit.objects.create(
            owner=self.user,
            place='В парке',
            time_start='14:30:00',
            action='Слушать музыку',
            nice=True,
            period=1,
            time_period=10,
            published=True
        )
    def test_create_habit(self):
        """Тест создание привычки"""
        data = {
            'place': 'Дом',
            'time_start': '14:30',
            'action': 'Пить чай',
            'nice': False,
            'period': 2,
            'time_period': 10
        }

        habit_create_url = reverse('habit:habit_create')
        response = self.client.post(habit_create_url, data=data)

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )
        print(response.json())

        self.assertEqual(
            response.json(),
            {
                'id': 2,
                'owner': None,
                'place': 'Дом',
                'time_start': '14:30:00',
                'action': 'Пить чай',
                'nice': False,
                'period': 2,
                'time_period': 10,
                'pleasant_habit': None,
                'published': False,
                'reward': None,
            }
        )

        self.assertTrue(
            Habit.objects.all().exists()
        )

    def test_list_habit(self):
        """Тест на вывод списка"""

        habit_list_url  = reverse('habit:habit_list')
        response = self.client.get(habit_list_url)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        print(response.json())
        self.assertEqual(
            Habit.objects.get(pk=self.habit.pk).action,
            response.json().get('results')[0].get('action'))

    def test_list_habit_public(self):
        """Тест на вывод списка публичных привычек"""

        public_habit_url = reverse('habit:habit_public')
        self.client.force_authenticate(user=self.user)
        response = self.client.get(public_habit_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)

    def test_retrieve_habit(self):
        """Тест на вывод одной привычки"""

        habit_one_url = reverse('habit:habit_ditail', args=[self.habit.pk])

        response = self.client.get(habit_one_url)
        print(response.json())

        self.assertEqual(
            response.status_code, status.HTTP_200_OK,
        )

        response = response.json()

        self.assertEqual(response.get('owner'), self.user.pk)
        self.assertEqual(response.get('place'), 'В парке')
        self.assertEqual(response.get('time_start'), '14:30:00')
        self.assertEqual(response.get('action'), 'Слушать музыку')

    def test_update_habit(self):
        """Тест на обновление привычки"""

        data = {
            'place': 'новое место',
            'action': 'новое действие',
        }

        habit_update_url = reverse('habit:habit_update', args=[self.habit.pk])

        response = self.client.patch(habit_update_url, data)

        print(response.json())

        self.assertEqual(
            response.status_code, status.HTTP_200_OK,
        )
        response = response.json()

        self.assertEqual(response.get('place'), 'новое место')
        self.assertEqual(response.get('action'), 'новое действие')

    def test_delete_habit(self):
        """Тест на удаление привычки"""

        habit_delete_url = reverse('habit:habit_delete', args=[self.habit.pk])

        response = self.client.delete(habit_delete_url)

        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT,
        )
        self.assertFalse(
            Habit.objects.all().exists(),
        )
