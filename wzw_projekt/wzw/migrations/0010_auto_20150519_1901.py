# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wzw', '0009_auto_20150519_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='name',
            field=models.CharField(max_length=128, blank=True),
        ),
    ]
