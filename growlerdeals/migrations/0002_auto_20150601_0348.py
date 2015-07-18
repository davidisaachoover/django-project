# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('growlerdeals', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brewery',
            name='city',
        ),
        migrations.RemoveField(
            model_name='brewery',
            name='state',
        ),
        migrations.RemoveField(
            model_name='brewery',
            name='street',
        ),
        migrations.RemoveField(
            model_name='brewery',
            name='zipcode',
        ),
    ]
