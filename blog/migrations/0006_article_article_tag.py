# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-08 12:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20170808_1104'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_tag',
            field=models.CharField(default='', max_length=50, verbose_name='日志标签'),
        ),
    ]
