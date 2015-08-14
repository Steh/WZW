# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('wzw', '0018_auto_20150527_1147'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cost', models.FloatField(help_text=b'Wert der Ausgabe', verbose_name=b'Ausgabe')),
            ],
        ),
        migrations.AlterField(
            model_name='expense',
            name='cost',
            field=models.FloatField(help_text=b'Wert der Ausgabe', verbose_name=b'Ausgabe'),
        ),
        migrations.AlterField(
            model_name='expense',
            name='costPersons',
            field=models.ManyToManyField(help_text=b'Personen auf die diese Ausgabe aufgeteilt wird.', to='wzw.Person', verbose_name=b'Teilhaber'),
        ),
        migrations.AlterField(
            model_name='expense',
            name='createDate',
            field=models.DateField(default=django.utils.timezone.now, help_text=b'Gibt an wann die Ausgabe erstellt wurde.', verbose_name=b'Erstellungsdatum'),
        ),
        migrations.AlterField(
            model_name='expense',
            name='debitDate',
            field=models.DateField(default=django.utils.timezone.now, verbose_name=b'Datum der Zahlung', blank=True),
        ),
        migrations.AlterField(
            model_name='expense',
            name='description',
            field=models.CharField(help_text=b'Beschreibung der Ausgabe (optional)', max_length=256, verbose_name=b'Beschreibung', blank=True),
        ),
        migrations.AlterField(
            model_name='expense',
            name='group',
            field=models.ForeignKey(verbose_name=b'Gruppe', to='wzw.Group', help_text=b'Zuordnung der Ausgabe zu einer Gruppe, kann nicht geaendert werden.'),
        ),
        migrations.AlterField(
            model_name='expense',
            name='name',
            field=models.CharField(help_text=b'Name der Ausgabe.', max_length=64, verbose_name=b'Name'),
        ),
        migrations.AlterField(
            model_name='expense',
            name='owner',
            field=models.ForeignKey(related_name='costOwner', verbose_name=b'Besitzer', to='wzw.Person', help_text=b'Wer hat das Geld ausgelegt?'),
        ),
        migrations.AlterField(
            model_name='group',
            name='description',
            field=models.CharField(default=b'', help_text=b'Beschreibung der Gruppe (optional)', max_length=128, verbose_name=b'Beschreibung', blank=True),
        ),
        migrations.AlterField(
            model_name='group',
            name='lastLogon',
            field=models.DateField(help_text=b'Gibt an wann die Gruppe das letzte mal aufgerufen wurde.(wird bei jedem Speichern aktualisiert)', verbose_name=b'Last Logon', auto_now=True),
        ),
        migrations.AlterField(
            model_name='group',
            name='name',
            field=models.CharField(default=b'', help_text=b'Name f\xc3\x83\xc2\xbcr die Gruppe (optional)', max_length=32, verbose_name=b'Gruppenname', blank=True),
        ),
        migrations.AlterField(
            model_name='group',
            name='token',
            field=models.CharField(help_text=b'Gruppen Token, dient zum Aufrufen der Gruppe (Format: 1234-1234-1234-1233', verbose_name=b'Gruppen Token', unique=True, max_length=19, editable=False),
        ),
        migrations.AlterField(
            model_name='person',
            name='group',
            field=models.ForeignKey(verbose_name=b'Gruppe', to='wzw.Group', help_text=b'Zuordnung der Person zu einer Gruppe, kann nicht geaendert werden.'),
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(help_text=b'Anzeigename der Person', max_length=64, verbose_name=b'Name'),
        ),
        migrations.AddField(
            model_name='report',
            name='costPerson',
            field=models.ForeignKey(related_name='report_cost_person', verbose_name=b'Schuldner', to='wzw.Person', help_text=b'Wer ist der Schuldner?'),
        ),
        migrations.AddField(
            model_name='report',
            name='group',
            field=models.ForeignKey(related_name='report_group', verbose_name=b'Gruppe', to='wzw.Group', help_text=b'Zuordnung der Ausgabe zu einer Gruppe, kann nicht geaendert werden.'),
        ),
        migrations.AddField(
            model_name='report',
            name='owner',
            field=models.ForeignKey(related_name='report_cost_owner', verbose_name=b'Besitzer', to='wzw.Person', help_text=b'Wer hat das Geld ausgelegt?'),
        ),
    ]
