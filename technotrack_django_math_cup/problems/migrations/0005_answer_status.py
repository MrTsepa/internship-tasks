# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-11 20:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0004_auto_20170911_1251'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='status',
            field=models.CharField(choices=[('OK', 'OK'), ('WA', 'Wrong answer'), ('WF', 'Wrong format'), ('ER', 'Error'), ('IP', 'In process')], default='IP', max_length=2),
        ),
    ]
