# Generated by Django 5.0 on 2023-12-16 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habit', '0006_alter_habit_period'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='nice',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Признак приятной привычки'),
        ),
    ]
