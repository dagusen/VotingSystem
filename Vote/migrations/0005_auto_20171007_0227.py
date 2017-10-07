# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-07 02:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Vote', '0004_auto_20171007_0206'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Student', to='Vote.Course'),
        ),
        migrations.AlterField(
            model_name='course',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Course', to='Vote.Department'),
        ),
    ]
