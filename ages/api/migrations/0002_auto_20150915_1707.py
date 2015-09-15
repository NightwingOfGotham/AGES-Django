# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fleet',
            name='name',
            field=models.CharField(unique=True, max_length=32),
        ),
        migrations.AlterField(
            model_name='officer',
            name='home_planet',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='officer',
            name='name',
            field=models.CharField(unique=True, max_length=32),
        ),
        migrations.AlterField(
            model_name='ship',
            name='name',
            field=models.CharField(unique=True, max_length=32),
        ),
    ]
