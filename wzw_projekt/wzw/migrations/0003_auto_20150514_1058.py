# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wzw', '0002_auto_20150514_1043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='lastLogon',
            field=models.DateField(auto_now=True, verbose_name=b'Last Logon'),
        ),
    ]
