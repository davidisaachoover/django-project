# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('growlerdeals', '0010_auto_20150601_1851'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brewery',
            name='address_line2',
        ),
        migrations.AddField(
            model_name='brewery',
            name='website',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='brewery',
            name='address_line1',
            field=models.CharField(max_length=50, verbose_name=b'Address line 1', blank=True),
        ),
    ]
