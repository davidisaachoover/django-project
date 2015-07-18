# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('growlerdeals', '0005_auto_20150601_0542'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brewery',
            name='deal_days',
        ),
        migrations.AddField(
            model_name='brewery',
            name='address_line1',
            field=models.CharField(max_length=45, verbose_name=b'Address line 1', blank=True),
        ),
        migrations.AddField(
            model_name='brewery',
            name='address_line2',
            field=models.CharField(max_length=45, verbose_name=b'Address line 2', blank=True),
        ),
        migrations.AddField(
            model_name='brewery',
            name='city',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AddField(
            model_name='brewery',
            name='postal_code',
            field=models.CharField(max_length=10, verbose_name=b'Postal Code', blank=True),
        ),
        migrations.AddField(
            model_name='brewery',
            name='state_province',
            field=models.CharField(max_length=40, verbose_name=b'State/Province', blank=True),
        ),
    ]
