# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-21 12:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0008_auto_20160821_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='open_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
