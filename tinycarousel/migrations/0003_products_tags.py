# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tinycarousel', '0002_auto_20160403_1707'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='tags',
            field=models.CharField(max_length=100, blank=True),
        ),
    ]
