# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('growlerdeals', '0027_auto_20150609_2251'),
    ]

    operations = [
        migrations.CreateModel(
            name='closed',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('monday', models.CharField(default=b'U', max_length=10, choices=[(b'U', b'Unknown'), (b'O', b'Open'), (b'C', b'Closed')])),
                ('tuesday', models.CharField(default=b'U', max_length=10, choices=[(b'U', b'Unknown'), (b'O', b'Open'), (b'C', b'Closed')])),
                ('wednesday', models.CharField(default=b'U', max_length=10, choices=[(b'U', b'Unknown'), (b'O', b'Open'), (b'C', b'Closed')])),
                ('thursday', models.CharField(default=b'U', max_length=10, choices=[(b'U', b'Unknown'), (b'O', b'Open'), (b'C', b'Closed')])),
                ('friday', models.CharField(default=b'U', max_length=10, choices=[(b'U', b'Unknown'), (b'O', b'Open'), (b'C', b'Closed')])),
                ('saturday', models.CharField(default=b'U', max_length=10, choices=[(b'U', b'Unknown'), (b'O', b'Open'), (b'C', b'Closed')])),
                ('sunday', models.CharField(default=b'U', max_length=10, choices=[(b'U', b'Unknown'), (b'O', b'Open'), (b'C', b'Closed')])),
                ('brewery', models.ForeignKey(to='growlerdeals.Brewery')),
            ],
        ),
        migrations.CreateModel(
            name='prices',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('monday', models.DecimalField(null=True, max_digits=4, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)])),
                ('tuesday', models.DecimalField(null=True, max_digits=4, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)])),
                ('wednesday', models.DecimalField(null=True, max_digits=4, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)])),
                ('thursday', models.DecimalField(null=True, max_digits=4, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)])),
                ('friday', models.DecimalField(null=True, max_digits=4, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)])),
                ('saturday', models.DecimalField(null=True, max_digits=4, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)])),
                ('sunday', models.DecimalField(null=True, max_digits=4, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)])),
                ('brewery', models.ForeignKey(to='growlerdeals.Brewery')),
            ],
        ),
    ]
