# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-11 12:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0002_problem_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]
