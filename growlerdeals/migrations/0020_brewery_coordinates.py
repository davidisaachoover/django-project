# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('growlerdeals', '0019_auto_20150602_1951'),
    ]

    operations = [
        migrations.AddField(
            model_name='brewery',
            name='coordinates',
            field=models.CharField(max_length=100, blank=True),
        ),
    ]
