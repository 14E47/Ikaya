# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-13 10:03
from __future__ import unicode_literals

from django.db import migrations, models
import oscar.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('custom_block', '0002_auto_20170713_0945'),
    ]

    operations = [
        migrations.AddField(
            model_name='customimage',
            name='link_url',
            field=oscar.models.fields.ExtendedURLField(blank=True, help_text='This is where this promotion links to', verbose_name='Link URL'),
        ),
        migrations.AlterField(
            model_name='customimage',
            name='button',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='Button Text'),
        ),
        migrations.AlterField(
            model_name='customimage',
            name='image',
            field=models.ImageField(blank=True, max_length=255, upload_to='/media/promotions/custom-image', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='customimage',
            name='name',
            field=models.CharField(blank=True, max_length=128, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='customimage',
            name='text',
            field=models.TextField(blank=True, verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='customimage',
            name='text_colour',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='Text Colour'),
        ),
    ]
