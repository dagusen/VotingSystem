# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-08 01:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Vote', '0019_partylist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='position',
            name='candidate',
        ),
        migrations.AddField(
            model_name='candidate',
            name='position',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Candidate', to='Vote.Position'),
        ),
    ]