# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('growlerdeals', '0036_auto_20150701_2108'),
    ]

    operations = [
        migrations.CreateModel(
            name='Displayed_prices',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Sunday', models.CharField(max_length=12)),
                ('Monday', models.CharField(max_length=12)),
                ('Tuesday', models.CharField(max_length=12)),
                ('Wednesday', models.CharField(max_length=12)),
                ('Thursday', models.CharField(max_length=12)),
                ('Friday', models.CharField(max_length=12)),
                ('Saturday', models.CharField(max_length=12)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('brewery', models.ForeignKey(to='growlerdeals.Brewery', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Graveyard_submissions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Sunday', models.DecimalField(null=True, max_digits=4, decimal_places=2, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('Monday', models.DecimalField(null=True, max_digits=4, decimal_places=2, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('Tuesday', models.DecimalField(null=True, max_digits=4, decimal_places=2, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('Wednesday', models.DecimalField(null=True, max_digits=4, decimal_places=2, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('Thursday', models.DecimalField(null=True, max_digits=4, decimal_places=2, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('Friday', models.DecimalField(null=True, max_digits=4, decimal_places=2, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('Saturday', models.DecimalField(null=True, max_digits=4, decimal_places=2, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('TimeSubmitted', models.DateTimeField(auto_now_add=True)),
                ('submitted_ip', models.GenericIPAddressField(null=True)),
                ('brewery', models.ForeignKey(to='growlerdeals.Brewery')),
            ],
        ),
    ]
