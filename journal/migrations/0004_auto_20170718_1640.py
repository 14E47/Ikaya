# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-18 16:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0003_journalyoutube'),
    ]

    operations = [
        migrations.AddField(
            model_name='journal',
            name='summary',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='journalyoutube',
            name='url',
            field=models.CharField(max_length=250),
        ),
    ]
