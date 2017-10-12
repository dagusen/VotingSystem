# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-12 00:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Position', '0002_auto_20171011_0844'),
        ('PartyList', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='partylist',
            name='position',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='PartyList', to='Position.Position'),
        ),
    ]