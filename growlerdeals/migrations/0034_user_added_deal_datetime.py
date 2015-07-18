# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('growlerdeals', '0033_auto_20150627_2212'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_added_deal',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 29, 17, 1, 54, 292242, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
