# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('growlerdeals', '0043_auto_20150705_1921'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_added_brewery',
            old_name='added_brewery_name',
            new_name='brewery_name',
        ),
        migrations.AddField(
            model_name='user_added_brewery',
            name='submitted_ip',
            field=models.GenericIPAddressField(null=True),
        ),
        migrations.AddField(
            model_name='user_added_brewery',
            name='time_submitted',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 8, 1, 26, 39, 61064, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
