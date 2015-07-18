# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('growlerdeals', '0004_auto_20150601_0438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brewery',
            name='deal_days',
            field=models.CharField(default=b'', max_length=1, blank=True, choices=[(0, b'Monday'), (1, b'Tuesday'), (2, b'Wednesday'), (3, b'Thursday'), (4, b'Friday'), (5, b'Saturday'), (6, b'Sunday')]),
        ),
        migrations.AlterField(
            model_name='brewery',
            name='notes',
            field=models.CharField(default=b'', max_length=250, blank=True),
        ),
    ]
