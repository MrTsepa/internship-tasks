# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-11 21:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cups', '0002_round_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='round',
            name='end_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='round',
            name='start_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
