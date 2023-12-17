# Generated by Django 5.0 on 2023-12-14 17:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Название привычки')),
                ('place', models.CharField(max_length=150, verbose_name='Место выполнения привычки')),
                ('time_start', models.DateTimeField(verbose_name='Время начала')),
                ('action', models.TextField(verbose_name='Действие привычки')),
                ('nice', models.BooleanField(verbose_name='Признак приятной привычки')),
                ('period', models.CharField(choices=[('DAILY', 'Daily'), ('WEEKLY', 'Weekly')], default='DAILY', max_length=50, verbose_name='Периодичность')),
                ('reward', models.TextField(blank=True, null=True, verbose_name='Вознаграждение')),
                ('time_period', models.PositiveIntegerField(verbose_name='Время на выполнение')),
                ('published', models.BooleanField(default=False, verbose_name='Признак публичности')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Создатель привычки')),
            ],
            options={
                'verbose_name': 'Привычка',
                'verbose_name_plural': 'Привычки',
            },
        ),
    ]
