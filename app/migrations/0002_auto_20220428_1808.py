# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-04-28 15:08
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2022, 4, 28, 18, 8, 34, 28133), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2022, 4, 28, 18, 8, 34, 28133), verbose_name='Дата комментария'),
        ),
    ]
