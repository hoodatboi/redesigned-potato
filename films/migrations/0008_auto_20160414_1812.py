# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-14 15:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0007_auto_20160414_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seans',
            name='time',
            field=models.CharField(max_length=30),
        ),
    ]
