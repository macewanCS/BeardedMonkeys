# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-04 19:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('epl', '0008_auto_20170322_1500'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='status',
            field=models.CharField(default='staff', max_length=20),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='branch',
            field=models.CharField(default='home', max_length=20),
        ),
    ]
