# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('growlerdeals', '0032_user_added_deal_sunday'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_added_deal',
            name='Friday',
            field=models.DecimalField(null=True, max_digits=4, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='user_added_deal',
            name='Monday',
            field=models.DecimalField(null=True, max_digits=4, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='user_added_deal',
            name='Saturday',
            field=models.DecimalField(null=True, max_digits=4, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='user_added_deal',
            name='Thursday',
            field=models.DecimalField(null=True, max_digits=4, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='user_added_deal',
            name='Tuesday',
            field=models.DecimalField(null=True, max_digits=4, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='user_added_deal',
            name='Wednesday',
            field=models.DecimalField(null=True, max_digits=4, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
