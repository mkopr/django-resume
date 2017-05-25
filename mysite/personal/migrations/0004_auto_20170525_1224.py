# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-25 12:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0003_remove_welcometext_add_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='basicinfo',
            old_name='url_1',
            new_name='github',
        ),
        migrations.RenameField(
            model_name='basicinfo',
            old_name='url_2',
            new_name='keybase',
        ),
        migrations.AddField(
            model_name='basicinfo',
            name='pdf_url',
            field=models.TextField(blank=True, default='link from cloud or drive', max_length=250, null=True),
        ),
    ]