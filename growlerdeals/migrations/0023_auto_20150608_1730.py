# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('growlerdeals', '0022_brewery_search_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brewery',
            name='closed_fri',
        ),
        migrations.RemoveField(
            model_name='brewery',
            name='closed_mon',
        ),
        migrations.RemoveField(
            model_name='brewery',
            name='closed_sat',
        ),
        migrations.RemoveField(
            model_name='brewery',
            name='closed_sun',
        ),
        migrations.RemoveField(
            model_name='brewery',
            name='closed_thu',
        ),
        migrations.RemoveField(
            model_name='brewery',
            name='closed_tue',
        ),
        migrations.RemoveField(
            model_name='brewery',
            name='closed_wed',
        ),
        migrations.RemoveField(
            model_name='brewery',
            name='coordinates',
        ),
        migrations.RemoveField(
            model_name='brewery',
            name='fri_price',
        ),
        migrations.RemoveField(
            model_name='brewery',
            name='full_address',
        ),
        migrations.RemoveField(
            model_name='brewery',
            name='mon_price',
        ),
        migrations.RemoveField(
            model_name='brewery',
            name='sat_price',
        ),
        migrations.RemoveField(
            model_name='brewery',
            name='sun_price',
        ),
        migrations.RemoveField(
            model_name='brewery',
            name='thu_price',
        ),
        migrations.RemoveField(
            model_name='brewery',
            name='tue_price',
        ),
        migrations.RemoveField(
            model_name='brewery',
            name='wed_price',
        ),
    ]
