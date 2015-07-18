# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('growlerdeals', '0044_auto_20150707_1826'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_added_deal',
            name='votes',
        ),
        migrations.AlterField(
            model_name='displayed_prices',
            name='Friday',
            field=models.CharField(max_length=12, blank=True),
        ),
        migrations.AlterField(
            model_name='displayed_prices',
            name='Monday',
            field=models.CharField(max_length=12, blank=True),
        ),
        migrations.AlterField(
            model_name='displayed_prices',
            name='Saturday',
            field=models.CharField(max_length=12, blank=True),
        ),
        migrations.AlterField(
            model_name='displayed_prices',
            name='Sunday',
            field=models.CharField(max_length=12, blank=True),
        ),
        migrations.AlterField(
            model_name='displayed_prices',
            name='Thursday',
            field=models.CharField(max_length=12, blank=True),
        ),
        migrations.AlterField(
            model_name='displayed_prices',
            name='Tuesday',
            field=models.CharField(max_length=12, blank=True),
        ),
        migrations.AlterField(
            model_name='displayed_prices',
            name='Wednesday',
            field=models.CharField(max_length=12, blank=True),
        ),
    ]
