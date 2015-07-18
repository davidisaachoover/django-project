# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('growlerdeals', '0037_displayed_prices_graveyard_submissions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='displayed_prices',
            name='brewery',
            field=models.OneToOneField(to='growlerdeals.Brewery'),
        ),
    ]
