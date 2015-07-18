# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('growlerdeals', '0011_auto_20150602_1722'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brewery',
            name='postal_code',
        ),
        migrations.AddField(
            model_name='brewery',
            name='zip_code',
            field=models.CharField(max_length=10, verbose_name=b'Zip Code', blank=True),
        ),
        migrations.AlterField(
            model_name='brewery',
            name='website',
            field=models.CharField(max_length=100, blank=True),
        ),
    ]
