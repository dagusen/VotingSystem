# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-07 04:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Vote', '0009_caditate'),
    ]

    operations = [
        migrations.AddField(
            model_name='caditate',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Vote.Student'),
        ),
    ]
