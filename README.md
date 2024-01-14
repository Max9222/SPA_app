# SPA_app
Веб приложение для приобретения новых полезных привычек.

Описание проекта:
    Создана модель Привычка со следующими полями:
        place -	Место выполнения привычки
        time_start - Время начала
        action - Действие привычки
        nice -	Признак приятной привычки
        period - Периодичность
        reward - Вознаграждение
        time_period - Время на выполнение
        published - Признак публичности
        owner -	Создатель привычки
        pleasant_habit - Приятная привычка

Возможности:
    - Добавление привычки
    - Эндпоинты механизма CRUD
    - Осуществлена интеграция с Telegram Bot
    - Настроена рассылка напоминаний (переодические задачи)

На базе фреймворка Django
    Так же были использованы следующие библиотеки:
        Python
        Django
        Django DRF
        PostgreSQL
        JWT
        django_filters
        Celery
        Celery-Beat
        Redis
        CORS
        Swagger

Проект разворачивается на платформе Docker и состоит из 5 контейнеров:
1. db
2. redis
3. app
4. celery
5. celery_beat    

Для работы проекта необходимо:
- Скачать проект с https://github.com/ и запустить с помощью вашей локальной машины при этом не забыв установить Docker
- Добавить переменные окружения в файл .env
- И в командной строке проекта сделать следующие шаги:
1. docker-compose build (Сборка образов)
2. docker run --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -d postgres (Создание db, пользователя и пароль)
3. docker-compose up (Запуск контейнеров)

Переменные окружения продублированы в файле .env.sample (Заполняем и все начинает работать)
    DB_NAME=
    POSTGRES_USER=
    POSTGRES_PASSWORD=
    PGDATA=
    SECRET_KEY=
    TELEGRAM_TOKEN=
    TELEGRAM_ID=

Настроена Валидация:
    - Исключить одновременный выбор связанной привычки и указания вознаграждения.
    - Время выполнения должно быть не больше 120 секунд.
    - В связанные привычки могут попадать только привычки с признаком приятной привычки.
    - У приятной привычки не может быть вознаграждения или связанной привычки.
    - Нельзя выполнять привычку реже, чем 1 раз в 7 дней.
Настроена Пагинация:
    - 10 элементов на 1 странице, максимальное кол-во страниц - 100

Права доступа:
    - Каждый пользователь имеет доступ только к своим привычкам по механизму CRUD.
    - Пользователь может видеть список публичных привычек без возможности их как-то редактировать или удалять.

Эндпоинты: можно посмотреть в Документации: по ссылке http://localhost:8000//swagger/

Безопасность: настроен CORS.
