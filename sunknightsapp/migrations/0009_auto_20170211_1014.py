# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-11 10:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sunknightsapp', '0008_auto_20170211_0154'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='questtaskuserconnector',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='questtaskuserconnector',
            name='task',
        ),
        migrations.RemoveField(
            model_name='questtaskuserconnector',
            name='user',
        ),
        migrations.DeleteModel(
            name='QuestTaskUserConnector',
        ),
    ]