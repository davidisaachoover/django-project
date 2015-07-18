# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('growlerdeals', '0045_auto_20150710_2029'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prices',
            name='brewery',
        ),
        migrations.AlterField(
            model_name='displayed_prices',
            name='Friday',
            field=models.CharField(default=b'unknown', max_length=12),
        ),
        migrations.AlterField(
            model_name='displayed_prices',
            name='Monday',
            field=models.CharField(default=b'unknown', max_length=12),
        ),
        migrations.AlterField(
            model_name='displayed_prices',
            name='Saturday',
            field=models.CharField(default=b'unknown', max_length=12),
        ),
        migrations.AlterField(
            model_name='displayed_prices',
            name='Sunday',
            field=models.CharField(default=b'unknown', max_length=12),
        ),
        migrations.AlterField(
            model_name='displayed_prices',
            name='Thursday',
            field=models.CharField(default=b'unknown', max_length=12),
        ),
        migrations.AlterField(
            model_name='displayed_prices',
            name='Tuesday',
            field=models.CharField(default=b'unknown', max_length=12),
        ),
        migrations.AlterField(
            model_name='displayed_prices',
            name='Wednesday',
            field=models.CharField(default=b'unknown', max_length=12),
        ),
        migrations.DeleteModel(
            name='prices',
        ),
    ]
