# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-14 14:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0005_auto_20160414_1716'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='image_height',
            field=models.PositiveIntegerField(blank=True, default='525', editable=False, null=True),
        ),
        migrations.AddField(
            model_name='film',
            name='image_width',
            field=models.PositiveIntegerField(blank=True, default='260', editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='film',
            name='image',
            field=models.ImageField(height_field='image_height', upload_to='static/films', width_field='image_width'),
        ),
    ]
