# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-01 11:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cups', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='round',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
    ]
