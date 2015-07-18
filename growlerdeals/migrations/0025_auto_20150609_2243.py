# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('growlerdeals', '0024_site_header_user_added_brewery_user_added_deal'),
    ]

    operations = [
        migrations.CreateModel(
            name='site_header_set',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Monday_line_1', models.CharField(max_length=50)),
                ('Monday_line_2', models.CharField(max_length=50, blank=True)),
                ('Tuesday_line_1', models.CharField(max_length=50)),
                ('Tuesday_line_2', models.CharField(max_length=50, blank=True)),
                ('Wednesday_line_1', models.CharField(max_length=50)),
                ('Wednesday_line_2', models.CharField(max_length=50, blank=True)),
                ('Thursday_line_1', models.CharField(max_length=50)),
                ('Thursday_line_2', models.CharField(max_length=50, blank=True)),
                ('Friday_line_1', models.CharField(max_length=50)),
                ('Friday_line_2', models.CharField(max_length=50, blank=True)),
                ('Saturday_line_1', models.CharField(max_length=50)),
                ('Saturday_line_2', models.CharField(max_length=50, blank=True)),
                ('Sunday_line_1', models.CharField(max_length=50)),
                ('Sunday_line_2', models.CharField(max_length=50, blank=True)),
            ],
        ),
        migrations.DeleteModel(
            name='site_header',
        ),
    ]
