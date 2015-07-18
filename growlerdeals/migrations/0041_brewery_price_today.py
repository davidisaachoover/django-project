# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('growlerdeals', '0040_auto_20150703_2344'),
    ]

    operations = [
        migrations.AddField(
            model_name='brewery',
            name='price_today',
            field=models.CharField(max_length=6, blank=True),
        ),
    ]
