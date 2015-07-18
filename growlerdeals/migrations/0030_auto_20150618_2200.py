# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('growlerdeals', '0029_auto_20150618_2154'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_added_deal',
            name='brewery',
        ),
        migrations.DeleteModel(
            name='user_added_deal',
        ),
    ]
