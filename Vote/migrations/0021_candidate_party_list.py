# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-08 01:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Vote', '0020_auto_20171008_0140'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='party_list',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Candidate', to='Vote.Partylist'),
        ),
    ]
