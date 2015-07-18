# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('growlerdeals', '0008_auto_20150601_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brewery',
            name='state',
            field=models.CharField(max_length=20, verbose_name=b'State (abbreviation)', blank=True),
        ),
    ]
