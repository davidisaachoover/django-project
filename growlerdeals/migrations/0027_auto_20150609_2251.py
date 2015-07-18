# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('growlerdeals', '0026_site_header_set_header_set_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site_header_set',
            name='Friday_line_1',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='site_header_set',
            name='Monday_line_1',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='site_header_set',
            name='Saturday_line_1',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='site_header_set',
            name='Sunday_line_1',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='site_header_set',
            name='Thursday_line_1',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='site_header_set',
            name='Tuesday_line_1',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='site_header_set',
            name='Wednesday_line_1',
            field=models.CharField(max_length=50, blank=True),
        ),
    ]
