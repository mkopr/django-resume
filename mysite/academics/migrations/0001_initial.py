# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-19 19:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Academics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=20)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('logo_url', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=50)),
                ('faculty', models.CharField(max_length=50)),
                ('responsibilities', models.TextField(max_length=250)),
            ],
        ),
    ]
