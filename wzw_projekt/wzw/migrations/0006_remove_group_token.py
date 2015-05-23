# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('wzw', '0005_auto_20150518_1818'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='token',
        ),
    ]
