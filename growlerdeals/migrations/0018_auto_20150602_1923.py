# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('growlerdeals', '0017_auto_20150602_1913'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='growler_prices',
            name='brewery_id',
        ),
        migrations.RemoveField(
            model_name='open_days',
            name='brewery_id',
        ),
        migrations.AddField(
            model_name='brewery',
            name='closed_fri',
            field=models.CharField(default=b'U', max_length=10, choices=[(b'U', b'Unknown'), (b'O', b'Open'), (b'C', b'Closed')]),
        ),
        migrations.AddField(
            model_name='brewery',
            name='closed_mon',
            field=models.CharField(default=b'U', max_length=10, choices=[(b'U', b'Unknown'), (b'O', b'Open'), (b'C', b'Closed')]),
        ),
        migrations.AddField(
            model_name='brewery',
            name='closed_sat',
            field=models.CharField(default=b'U', max_length=10, choices=[(b'U', b'Unknown'), (b'O', b'Open'), (b'C', b'Closed')]),
        ),
        migrations.AddField(
            model_name='brewery',
            name='closed_sun',
            field=models.CharField(default=b'U', max_length=10, choices=[(b'U', b'Unknown'), (b'O', b'Open'), (b'C', b'Closed')]),
        ),
        migrations.AddField(
            model_name='brewery',
            name='closed_thu',
            field=models.CharField(default=b'U', max_length=10, choices=[(b'U', b'Unknown'), (b'O', b'Open'), (b'C', b'Closed')]),
        ),
        migrations.AddField(
            model_name='brewery',
            name='closed_tue',
            field=models.CharField(default=b'U', max_length=10, choices=[(b'U', b'Unknown'), (b'O', b'Open'), (b'C', b'Closed')]),
        ),
        migrations.AddField(
            model_name='brewery',
            name='closed_wed',
            field=models.CharField(default=b'U', max_length=10, choices=[(b'U', b'Unknown'), (b'O', b'Open'), (b'C', b'Closed')]),
        ),
        migrations.AddField(
            model_name='brewery',
            name='fri_price',
            field=models.DecimalField(null=True, max_digits=4, decimal_places=2),
        ),
        migrations.AddField(
            model_name='brewery',
            name='mon_price',
            field=models.DecimalField(null=True, max_digits=4, decimal_places=2),
        ),
        migrations.AddField(
            model_name='brewery',
            name='sat_price',
            field=models.DecimalField(null=True, max_digits=4, decimal_places=2),
        ),
        migrations.AddField(
            model_name='brewery',
            name='sun_price',
            field=models.DecimalField(null=True, max_digits=4, decimal_places=2),
        ),
        migrations.AddField(
            model_name='brewery',
            name='thu_price',
            field=models.DecimalField(null=True, max_digits=4, decimal_places=2),
        ),
        migrations.AddField(
            model_name='brewery',
            name='tue_price',
            field=models.DecimalField(null=True, max_digits=4, decimal_places=2),
        ),
        migrations.AddField(
            model_name='brewery',
            name='wed_price',
            field=models.DecimalField(null=True, max_digits=4, decimal_places=2),
        ),
        migrations.DeleteModel(
            name='Growler_prices',
        ),
        migrations.DeleteModel(
            name='open_days',
        ),
    ]
