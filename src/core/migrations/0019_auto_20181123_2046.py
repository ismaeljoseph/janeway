# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-23 20:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_auto_20181116_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='article_id',
            field=models.PositiveIntegerField(verbose_name='Article PK'),
        ),
    ]