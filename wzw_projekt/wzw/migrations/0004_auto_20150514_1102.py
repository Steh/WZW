# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('wzw', '0003_auto_20150514_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenses',
            name='createDate',
            field=models.DateField(verbose_name=b'date published'),
        ),
        migrations.AlterField(
            model_name='expenses',
            name='debitDate',
            field=models.DateField(verbose_name=b'date debited'),
        ),
    ]
