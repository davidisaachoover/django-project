# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('growlerdeals', '0006_auto_20150601_1838'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brewery',
            name='state_province',
        ),
        migrations.AddField(
            model_name='brewery',
            name='state',
            field=models.CharField(max_length=40, verbose_name=b'State', blank=True),
        ),
    ]
