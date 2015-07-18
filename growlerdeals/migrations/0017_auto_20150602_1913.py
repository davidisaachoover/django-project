# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('growlerdeals', '0016_auto_20150602_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='open_days',
            name='closed_sun',
            field=models.CharField(default=b'U', max_length=10, choices=[(b'U', b'Unknown'), (b'O', b'Open'), (b'C', b'Closed')]),
        ),
    ]
