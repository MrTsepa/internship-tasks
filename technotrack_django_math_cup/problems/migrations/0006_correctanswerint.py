# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-11 21:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0005_answer_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='CorrectAnswerInt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField()),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='problems.Problem')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
