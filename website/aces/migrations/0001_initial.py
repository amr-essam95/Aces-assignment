# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-23 22:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='applicants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('mobilenumber', models.CharField(max_length=30)),
            ],
        ),
    ]
