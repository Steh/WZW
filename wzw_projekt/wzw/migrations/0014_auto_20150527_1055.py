# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('wzw', '0013_auto_20150522_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='createDate',
            field=models.DateField(default=django.utils.timezone.now, verbose_name=b'date published'),
        ),
        migrations.AlterField(
            model_name='expense',
            name='debitDate',
            field=models.DateField(default=django.utils.timezone.now, verbose_name=b'date debited', blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='id',
            field=models.IntegerField(max_length=192, serialize=False, primary_key=True),
        ),
    ]
