# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('growlerdeals', '0014_auto_20150602_1900'),
    ]

    operations = [
        migrations.CreateModel(
            name='open_days',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('closed_sun', models.CharField(default=b'U', max_length=10, choices=[(b'U', b'Unknown'), (b'O', b'Open'), (b'C', b'Closed')])),
                ('closed_mon', models.BooleanField()),
                ('closed_tue', models.BooleanField()),
                ('closed_wed', models.BooleanField()),
                ('closed_thu', models.BooleanField()),
                ('closed_fri', models.BooleanField()),
                ('closed_sat', models.BooleanField()),
                ('brewery_id', models.ForeignKey(to='growlerdeals.Brewery')),
            ],
        ),
        migrations.RemoveField(
            model_name='growler_prices',
            name='closed_fri',
        ),
        migrations.RemoveField(
            model_name='growler_prices',
            name='closed_mon',
        ),
        migrations.RemoveField(
            model_name='growler_prices',
            name='closed_sat',
        ),
        migrations.RemoveField(
            model_name='growler_prices',
            name='closed_sun',
        ),
        migrations.RemoveField(
            model_name='growler_prices',
            name='closed_thu',
        ),
        migrations.RemoveField(
            model_name='growler_prices',
            name='closed_tue',
        ),
        migrations.RemoveField(
            model_name='growler_prices',
            name='closed_wed',
        ),
    ]
