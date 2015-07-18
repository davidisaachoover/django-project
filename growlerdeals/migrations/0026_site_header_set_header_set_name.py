# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('growlerdeals', '0025_auto_20150609_2243'),
    ]

    operations = [
        migrations.AddField(
            model_name='site_header_set',
            name='header_set_name',
            field=models.CharField(default=b'default', max_length=25),
        ),
    ]
