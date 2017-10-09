# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-07 05:12
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Vote', '0018_auto_20171007_0503'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partylist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partylist_name', models.CharField(max_length=200)),
                ('goals', models.TextField(max_length=3000)),
                ('projects', models.TextField(max_length=3000)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]