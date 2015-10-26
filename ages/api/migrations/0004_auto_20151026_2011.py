# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20150915_1737'),
    ]

    operations = [
        migrations.AddField(
            model_name='fleet',
            name='fleet_number',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='officer',
            name='rank',
            field=models.CharField(default=b'ENS', max_length=4, choices=[(b'ADM', b'Admiral'), (b'FCPT', b'Fleet Captain'), (b'CAPT', b'Captain'), (b'CDR', b'Commander'), (b'LEF', b'Leftenant'), (b'ENS', b'Ensign')]),
        ),
    ]
