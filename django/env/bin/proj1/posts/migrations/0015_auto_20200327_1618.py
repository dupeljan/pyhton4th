# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2020-03-27 13:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0014_auto_20200327_1444'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpaceObject',
            fields=[
                ('idobject', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=120)),
                ('radius', models.FloatField()),
                ('mass', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='SpaceObjectType',
            fields=[
                ('idtype', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='SpaceSystem',
            fields=[
                ('idsystem', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=120)),
                ('size', models.FloatField()),
            ],
        ),
        migrations.RemoveField(
            model_name='comment',
            name='comment_article',
        ),
        migrations.RemoveField(
            model_name='post',
            name='post_author',
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.AddField(
            model_name='spaceobject',
            name='system_idsystem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.SpaceSystem'),
        ),
        migrations.AddField(
            model_name='spaceobject',
            name='type_idtye',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.SpaceObjectType'),
        ),
    ]