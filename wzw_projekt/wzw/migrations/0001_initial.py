# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expenses',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=256, blank=True)),
                ('createDate', models.DateTimeField(verbose_name=b'date published')),
                ('debitDate', models.DateTimeField(verbose_name=b'date debited')),
                ('cost', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('lastLogon', models.DateField(verbose_name=b'date logon', blank=True)),
                ('email', models.EmailField(max_length=254, blank=True)),
                ('pwd', models.CharField(max_length=32, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name='expenses',
            name='costPersons',
            field=models.ManyToManyField(to='wzw.Person'),
        ),
        migrations.AddField(
            model_name='expenses',
            name='group',
            field=models.ForeignKey(to='wzw.Group'),
        ),
        migrations.AddField(
            model_name='expenses',
            name='owner',
            field=models.ForeignKey(related_name='costOwner', to='wzw.Person'),
        ),
    ]
