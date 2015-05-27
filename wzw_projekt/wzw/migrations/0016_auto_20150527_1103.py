# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wzw', '0015_auto_20150527_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='id',
            field=models.IntegerField(max_length=192, serialize=False, primary_key=True),
        ),
    ]
