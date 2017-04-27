# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-09 10:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=11, unique=True)),
                ('last_login', models.CharField(max_length=50)),
            ],
        ),
    ]
