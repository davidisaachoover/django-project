# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('growlerdeals', '0042_auto_20150705_1917'),
    ]

    operations = [
        migrations.CreateModel(
            name='Displayed_prices',
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
            model_name='displayedprices',
            name='brewery',
        ),
        migrations.DeleteModel(
            name='DisplayedPrices',
        ),
    ]
