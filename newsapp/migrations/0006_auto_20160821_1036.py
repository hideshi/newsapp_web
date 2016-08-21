# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-21 10:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0005_auto_20160821_0727'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='notify',
            field=models.CharField(choices=[('yes', 'Yes'), ('no', 'Np')], default='yes', max_length=8),
        ),
        migrations.AlterField(
            model_name='article',
            name='open_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('public', 'Public')], default='draft', max_length=8),
        ),
    ]
