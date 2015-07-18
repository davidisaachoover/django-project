# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('growlerdeals', '0013_growler_prices'),
    ]

    operations = [
        migrations.AlterField(
            model_name='growler_prices',
            name='closed_sun',
            field=models.CharField(default=b'U', max_length=10, choices=[(b'U', b'Unknown'), (b'O', b'Open'), (b'C', b'Closed')]),
        ),
    ]
