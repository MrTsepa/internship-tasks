# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-11 12:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0003_auto_20170911_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
