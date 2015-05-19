# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wzw', '0007_group_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='token',
            field=models.CharField(unique=True, max_length=19, editable=False),
        ),
    ]
