# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-22 12:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20171122_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='rfid',
            field=models.CharField(max_length=16, unique=True),
        ),
    ]