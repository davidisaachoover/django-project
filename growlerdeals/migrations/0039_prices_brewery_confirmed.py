# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('growlerdeals', '0038_auto_20150702_2156'),
    ]

    operations = [
        migrations.AddField(
            model_name='prices',
            name='brewery_confirmed',
            field=models.BooleanField(default=False),
        ),
    ]
