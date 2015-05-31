# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('wzw', '0016_auto_20150527_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
    ]
