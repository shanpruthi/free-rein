# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-03 17:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tinycarousel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='description',
            field=models.TextField(max_length=400),
        ),
    ]
