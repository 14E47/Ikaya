# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-14 06:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_block', '0004_auto_20170713_1005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customimage',
            name='image',
            field=models.ImageField(blank=True, max_length=255, upload_to=b'images/promotions/', verbose_name='Image'),
        ),
    ]
