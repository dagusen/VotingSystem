# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-07 04:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Vote', '0011_auto_20171007_0420'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cadidate',
            new_name='Candidate',
        ),
    ]
