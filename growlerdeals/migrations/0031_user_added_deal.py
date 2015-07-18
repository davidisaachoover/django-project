# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('growlerdeals', '0030_auto_20150618_2200'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_added_deal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('votes', models.IntegerField(default=1)),
                ('submitted_ip', models.GenericIPAddressField(null=True)),
                ('brewery', models.ForeignKey(to='growlerdeals.Brewery')),
            ],
        ),
    ]
