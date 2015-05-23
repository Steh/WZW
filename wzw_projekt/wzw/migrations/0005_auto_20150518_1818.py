# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('wzw', '0004_auto_20150514_1102'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='token',
            field=models.CharField(default=-2468, unique=True, max_length=19, editable=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='expenses',
            name='costPersons',
            field=models.ManyToManyField(to='wzw.Person', blank=True),
        ),
        migrations.AlterField(
            model_name='expenses',
            name='debitDate',
            field=models.DateField(verbose_name=b'date debited', blank=True),
        ),
    ]
