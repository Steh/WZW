# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('wzw', '0008_auto_20150519_1827'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='email',
        ),
        migrations.RemoveField(
            model_name='group',
            name='pwd',
        ),
    ]
