# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-03 00:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_id', models.CharField(max_length=22)),
                ('video_id1', models.CharField(max_length=22)),
                ('video_id2', models.CharField(max_length=22)),
            ],
        ),
    ]
