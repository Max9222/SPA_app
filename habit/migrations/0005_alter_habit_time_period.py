# Generated by Django 5.0 on 2023-12-16 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habit', '0004_alter_habit_time_period'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='time_period',
            field=models.IntegerField(blank=True, null=True, verbose_name='Время на выполнение'),
        ),
    ]
