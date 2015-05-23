# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('wzw', '0006_remove_group_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='token',
            field=models.CharField(default=-2468, max_length=19, editable=False),
            preserve_default=False,
        ),
    ]
