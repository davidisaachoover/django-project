# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('growlerdeals', '0003_auto_20150601_0435'),
    ]

    operations = [
        migrations.RenameField(
            model_name='brewery',
            old_name='days',
            new_name='deal_days',
        ),
    ]
