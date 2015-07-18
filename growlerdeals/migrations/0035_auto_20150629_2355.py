# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('growlerdeals', '0034_user_added_deal_datetime'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_added_deal',
            old_name='datetime',
            new_name='TimeSubmitted',
        ),
    ]
