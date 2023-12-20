import requests
from django.conf import settings

from config.settings import TELEGRAM_ID
def tg_send_message(chat_id, text):
    """Отправка сообщения в телеграм"""
    params = {'chat_id': chat_id, 'text': text}
    requests.post(f'https://api.telegram.org/bot{settings.TELEGRAM_TOKEN}/sendMessage', params=params)

class MyBot:
    URL = 'https://api.telegram.org/bot'
    TOKEN = settings.TELEGRAM_TOKEN

    def send_massage(self, text):
        requests.post(
            url=f'{self.URL}{self.TOKEN}/sendMessage',
            data={
                'chat_id': TELEGRAM_ID,
                'text': text
            }
        )
