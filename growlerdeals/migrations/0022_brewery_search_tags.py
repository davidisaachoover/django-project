# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('growlerdeals', '0021_brewery_full_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='brewery',
            name='search_tags',
            field=models.CharField(max_length=250, blank=True),
        ),
    ]
