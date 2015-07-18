# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('growlerdeals', '0023_auto_20150608_1730'),
    ]

    operations = [
        migrations.CreateModel(
            name='site_header',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('header_line1', models.CharField(max_length=50)),
                ('header_line2', models.CharField(max_length=50, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='user_added_brewery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('added_brewery_name', models.CharField(max_length=200)),
                ('website', models.CharField(max_length=100, blank=True)),
                ('address_line1', models.CharField(max_length=50, verbose_name=b'Address line 1', blank=True)),
                ('city', models.CharField(max_length=50, blank=True)),
                ('state', models.CharField(max_length=2, verbose_name=b'State (abbreviation)', blank=True)),
                ('zip_code', models.CharField(max_length=10, verbose_name=b'Zip Code', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='user_added_deal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sun_price', models.DecimalField(null=True, max_digits=4, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)])),
                ('mon_price', models.DecimalField(null=True, max_digits=4, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)])),
                ('tue_price', models.DecimalField(null=True, max_digits=4, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)])),
                ('wed_price', models.DecimalField(null=True, max_digits=4, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)])),
                ('thu_price', models.DecimalField(null=True, max_digits=4, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)])),
                ('fri_price', models.DecimalField(null=True, max_digits=4, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)])),
                ('sat_price', models.DecimalField(null=True, max_digits=4, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)])),
                ('notes', models.CharField(default=b'', max_length=250, blank=True)),
                ('brewery', models.ForeignKey(to='growlerdeals.Brewery')),
            ],
        ),
    ]
