# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.db import models, migrations
from django.utils.timezone import utc


class Migration(migrations.Migration):
    dependencies = [
        ('wzw', '0012_auto_20150521_0848'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='description',
            field=models.CharField(default=b'', max_length=128, blank=True),
        ),
        migrations.AlterField(
            model_name='expense',
            name='costPersons',
            field=models.ManyToManyField(to='wzw.Person', verbose_name=b'costPerson_PersonId', blank=True),
        ),
        migrations.AlterField(
            model_name='expense',
            name='createDate',
            field=models.DateField(default=datetime.datetime(2015, 5, 22, 14, 5, 38, 741974, tzinfo=utc),
                                   verbose_name=b'date published'),
        ),
        migrations.AlterField(
            model_name='expense',
            name='debitDate',
            field=models.DateField(default=datetime.datetime(2015, 5, 22, 14, 5, 38, 742404, tzinfo=utc),
                                   verbose_name=b'date debited', blank=True),
        ),
        migrations.AlterField(
            model_name='group',
            name='name',
            field=models.CharField(default=b'', max_length=32, blank=True),
        ),
    ]
