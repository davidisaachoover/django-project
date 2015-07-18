# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('growlerdeals', '0028_closed_prices'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_added_deal',
            old_name='fri_price',
            new_name='Friday',
        ),
        migrations.RenameField(
            model_name='user_added_deal',
            old_name='mon_price',
            new_name='Monday',
        ),
        migrations.RenameField(
            model_name='user_added_deal',
            old_name='sat_price',
            new_name='Saturday',
        ),
        migrations.RenameField(
            model_name='user_added_deal',
            old_name='sun_price',
            new_name='Sunday',
        ),
        migrations.RenameField(
            model_name='user_added_deal',
            old_name='thu_price',
            new_name='Thursday',
        ),
        migrations.RenameField(
            model_name='user_added_deal',
            old_name='tue_price',
            new_name='Tuesday',
        ),
        migrations.RenameField(
            model_name='user_added_deal',
            old_name='wed_price',
            new_name='Wednesday',
        ),
        migrations.RemoveField(
            model_name='user_added_deal',
            name='notes',
        ),
        migrations.AddField(
            model_name='user_added_deal',
            name='submitted_ip',
            field=models.GenericIPAddressField(null=True),
        ),
        migrations.AddField(
            model_name='user_added_deal',
            name='votes',
            field=models.IntegerField(default=1),
        ),
    ]
