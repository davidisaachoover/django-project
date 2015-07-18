# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('growlerdeals', '0012_auto_20150602_1737'),
    ]

    operations = [
        migrations.CreateModel(
            name='Growler_prices',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('closed_sun', models.BooleanField()),
                ('closed_mon', models.BooleanField()),
                ('closed_tue', models.BooleanField()),
                ('closed_wed', models.BooleanField()),
                ('closed_thu', models.BooleanField()),
                ('closed_fri', models.BooleanField()),
                ('closed_sat', models.BooleanField()),
                ('sun_price', models.DecimalField(max_digits=4, decimal_places=2)),
                ('mon_price', models.DecimalField(max_digits=4, decimal_places=2)),
                ('tue_price', models.DecimalField(max_digits=4, decimal_places=2)),
                ('wed_price', models.DecimalField(max_digits=4, decimal_places=2)),
                ('thu_price', models.DecimalField(max_digits=4, decimal_places=2)),
                ('fri_price', models.DecimalField(max_digits=4, decimal_places=2)),
                ('sat_price', models.DecimalField(max_digits=4, decimal_places=2)),
                ('brewery_id', models.ForeignKey(to='growlerdeals.Brewery')),
            ],
        ),
    ]
