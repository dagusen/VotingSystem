# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-07 01:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Vote', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Course', to='Vote.Department'),
        ),
    ]