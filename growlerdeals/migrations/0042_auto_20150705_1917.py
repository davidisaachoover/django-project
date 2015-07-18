# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('growlerdeals', '0041_brewery_price_today'),
    ]

    operations = [
        migrations.CreateModel(
            name='DisplayedPrices',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Sunday', models.CharField(max_length=12)),
                ('Monday', models.CharField(max_length=12)),
                ('Tuesday', models.CharField(max_length=12)),
                ('Wednesday', models.CharField(max_length=12)),
                ('Thursday', models.CharField(max_length=12)),
                ('Friday', models.CharField(max_length=12)),
                ('Saturday', models.CharField(max_length=12)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('brewery_confirmed', models.BooleanField(default=False)),
                ('brewery', models.OneToOneField(to='growlerdeals.Brewery')),
            ],
        ),
        migrations.RemoveField(
            model_name='displayed_prices',
            name='brewery',
        ),
        migrations.DeleteModel(
            name='Displayed_prices',
        ),
    ]
