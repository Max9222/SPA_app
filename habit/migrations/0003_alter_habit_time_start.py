# Generated by Django 5.0 on 2023-12-14 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habit', '0002_habit_pleasant_habit_alter_habit_period'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='time_start',
            field=models.TimeField(blank=True, null=True, verbose_name='Время начала'),
        ),
    ]
