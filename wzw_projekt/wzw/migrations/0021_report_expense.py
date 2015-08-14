# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wzw', '0020_report_payed'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='expense',
            field=models.ForeignKey(default=0, to='wzw.Expense'),
            preserve_default=False,
        ),
    ]
