# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('growlerdeals', '0039_prices_brewery_confirmed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='closed',
            name='brewery',
        ),
        migrations.AddField(
            model_name='displayed_prices',
            name='brewery_confirmed',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='closed',
        ),
    ]
