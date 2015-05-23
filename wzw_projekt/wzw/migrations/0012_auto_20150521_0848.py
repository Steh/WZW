# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wzw', '0011_auto_20150521_0843'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=256, blank=True)),
                ('createDate', models.DateField(verbose_name=b'date published')),
                ('debitDate', models.DateField(verbose_name=b'date debited', blank=True)),
                ('cost', models.FloatField()),
                ('costPersons', models.ManyToManyField(to='wzw.Person', blank=True)),
                ('group', models.ForeignKey(to='wzw.Group')),
                ('owner', models.ForeignKey(related_name='costOwner', to='wzw.Person')),
            ],
        ),
        migrations.RemoveField(
            model_name='expenses',
            name='costPersons',
        ),
        migrations.RemoveField(
            model_name='expenses',
            name='group',
        ),
        migrations.RemoveField(
            model_name='expenses',
            name='owner',
        ),
        migrations.DeleteModel(
            name='Expenses',
        ),
    ]
