# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import re
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fleet',
            fields=[
                ('fleet_id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=32, validators=[django.core.validators.RegexValidator(re.compile('^[-a-zA-Z0-9_]+\\Z'), "Enter a valid 'slug' consisting of letters, numbers, underscores or hyphens.", 'invalid')])),
                ('motto', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Officer',
            fields=[
                ('officer_id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=32, validators=[django.core.validators.RegexValidator(re.compile('^[-a-zA-Z0-9_]+\\Z'), "Enter a valid 'slug' consisting of letters, numbers, underscores or hyphens.", 'invalid')])),
                ('rank', models.CharField(default=b'ENS', max_length=4, choices=[(b'ADM', b'Admiral'), (b'CAPT', b'Captain'), (b'CDR', b'Commander'), (b'LEF', b'Leftenant'), (b'ENS', b'Ensign')])),
                ('home_planet', models.CharField(max_length=32, validators=[django.core.validators.RegexValidator(re.compile('^[-a-zA-Z0-9_]+\\Z'), "Enter a valid 'slug' consisting of letters, numbers, underscores or hyphens.", 'invalid')])),
            ],
        ),
        migrations.CreateModel(
            name='Ship',
            fields=[
                ('ship_id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=32, validators=[django.core.validators.RegexValidator(re.compile('^[-a-zA-Z0-9_]+\\Z'), "Enter a valid 'slug' consisting of letters, numbers, underscores or hyphens.", 'invalid')])),
                ('fleet', models.ForeignKey(to='api.Fleet')),
            ],
        ),
        migrations.AddField(
            model_name='officer',
            name='ship',
            field=models.ForeignKey(to='api.Ship'),
        ),
    ]
