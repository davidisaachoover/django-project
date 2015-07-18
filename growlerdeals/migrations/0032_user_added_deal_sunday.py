# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('growlerdeals', '0031_user_added_deal'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_added_deal',
            name='Sunday',
            field=models.DecimalField(null=True, max_digits=4, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
