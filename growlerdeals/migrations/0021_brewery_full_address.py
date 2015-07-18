# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('growlerdeals', '0020_brewery_coordinates'),
    ]

    operations = [
        migrations.AddField(
            model_name='brewery',
            name='full_address',
            field=models.CharField(max_length=250, blank=True),
        ),
    ]
