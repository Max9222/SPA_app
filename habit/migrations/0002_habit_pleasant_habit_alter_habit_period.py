# Generated by Django 5.0 on 2023-12-14 17:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habit', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='habit',
            name='pleasant_habit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='habit.habit', verbose_name='Приятная привычка'),
        ),
        migrations.AlterField(
            model_name='habit',
            name='period',
            field=models.CharField(choices=[('DAILY', 'каждый день'), ('WEEKLY', 'раз в неделю')], default='DAILY', max_length=50, verbose_name='Периодичность'),
        ),
    ]
