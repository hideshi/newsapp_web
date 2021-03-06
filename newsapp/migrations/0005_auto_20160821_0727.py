# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-21 07:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0004_auto_20160821_0720'),
    ]

    operations = [
        migrations.RenameField(
            model_name='help',
            old_name='description',
            new_name='description_android',
        ),
        migrations.RenameField(
            model_name='termsofservice',
            old_name='description',
            new_name='description_android',
        ),
        migrations.AddField(
            model_name='help',
            name='description_ios',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='termsofservice',
            name='description_ios',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
