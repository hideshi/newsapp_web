# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-21 06:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0002_auto_20160821_0617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.CharField(choices=[('draft', '下書き'), ('public', '公開')], default='draft', max_length=8),
        ),
    ]