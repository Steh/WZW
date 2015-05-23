# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('wzw', '0010_auto_20150519_1901'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='group',
            field=models.ForeignKey(default=1, to='wzw.Group'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='group',
            name='name',
            field=models.CharField(max_length=32, blank=True),
        ),
    ]
