# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-16 16:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sunknightsapp', '0009_auto_20170211_1014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='helpinfo',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]