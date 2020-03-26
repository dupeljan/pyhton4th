# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2020-03-26 12:28
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_post_post_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 26, 15, 28, 10, 888809), verbose_name='Время создания'),
        ),
        migrations.AlterField(
            model_name='post',
            name='updated',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Время обновления'),
        ),
    ]
