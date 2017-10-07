# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-07 04:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Vote', '0012_auto_20171007_0421'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='candidate',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
