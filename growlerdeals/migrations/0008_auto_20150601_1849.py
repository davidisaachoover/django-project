# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('growlerdeals', '0007_auto_20150601_1841'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brewery',
            name='postal_code',
        ),
        migrations.AddField(
            model_name='brewery',
            name='Zip_code',
            field=models.CharField(max_length=10, verbose_name=b'Zip Code', blank=True),
        ),
        migrations.AlterField(
            model_name='brewery',
            name='state',
            field=models.CharField(max_length=2, verbose_name=b'State (abbreviation)', blank=True),
        ),
    ]
