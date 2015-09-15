# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20150915_1707'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fleet',
            name='fleet_id',
        ),
        migrations.RemoveField(
            model_name='officer',
            name='officer_id',
        ),
        migrations.RemoveField(
            model_name='ship',
            name='ship_id',
        ),
        migrations.AddField(
            model_name='fleet',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=1, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='officer',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=2, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ship',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=3, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
