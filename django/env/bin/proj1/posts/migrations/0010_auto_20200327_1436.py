# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2020-03-27 11:36
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_auto_20200327_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 27, 14, 36, 9, 308886), verbose_name='Время создания'),
        ),
    ]
