# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-20 10:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experience', '0002_auto_20170520_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='responsibilities',
            field=models.TextField(max_length=500),
        ),
    ]
