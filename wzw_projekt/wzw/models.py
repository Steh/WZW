# -*- coding: utf-8 -*-

"""
Datenmodele

Attribute der Attribute:
max_length:     maximale laenge
blank:          Darf leer sein
default:        Standart wert
verbose_name:   Anzeige Name in Formularen
help_text:      Hilfetext wird in Formularen angezeigt, dient als dokumentation der Felder
auto_now:       Beim Speichern wird das aktuelle Datum gespeichert
unique:         Muss eindeutig sein
editable:       Bearbeitbar
"""

from django.utils import timezone
from django.db import models

from wzw.functions import create_token


class Group(models.Model):
    # Definition der einzelnen Eingabefelder fÃ¼r die Gruppen auf den Gruppenunterseiten
    name = models.CharField(max_length=32,
                            blank=True,
                            default='',
                            verbose_name="Gruppenname",
                            help_text="Name fÃ¼r die Gruppe (optional)")
    description = models.CharField(max_length=128,
                                   blank=True,
                                   default='',
                                   verbose_name="Beschreibung",
                                   help_text="Beschreibung der Gruppe (optional)")
    token = models.CharField(max_length=19,
                             editable=False,
                             unique=True,
                             verbose_name="Gruppen Token",
                             help_text="Gruppen Token, dient zum Aufrufen der Gruppe (Format: 1234-1234-1234-1233")
    lastLogon = models.DateField('Last Logon',
                                 auto_now=True,
                                 blank=False,
                                 help_text="Gibt an wann die Gruppe das letzte mal aufgerufen wurde.(wird bei jedem Speichern aktualisiert)")

    '''
    # Rueckgabewert bei aufruf des Objekts
    '''

    def __str__(self):  # __unicode__ on Python 2
        return self.token

    '''
    # ueberschreibt die speichern methode
    # wenn die Gruppe neu erstellt wurde (kein primary key vorhanden)
    # wird ein token generiert und eingetragen
    '''

    def save(self, *args, **kwargs):
        if not self.pk:
            self.token = create_token()

        super(Group, self).save(*args, **kwargs)

    '''
    # ueberschreibt die loeschen methode
    # dadurch werden auch alle kosten + personen geloescht
    1. loeschen aller Personen die zu dieser Gruppe gehoeren
    2. loeschen aller Personen die zu dieser Gruppe gehoeren
    3. loeschen der Gruppe
    4. aufrufen der Original loeschen methode
    '''

    def delete(self, using=None):
        expense = Expense.objects.filter(group=self)
        expense.delete()

        person = Person.objects.filter(group=self)
        person.delete()

        super(Group, self).delete()

    '''
    Function to generate Report for Group
    '''
    def generate_report(self):
        report = Report.objects.filter(group=self)

        if report.count > 0:
            report.delete()

        expenses = Expense.objects.filter(group=self)

        for e in expenses:
            cost = e.cost / (e.costPersons.count())
            for person in e.costPersons.all():
                if person != e.owner:
                    report = Report(group=self, owner=e.owner, costPerson=person, expense=e, cost=cost, payed=0)
                    report.save()

    def validate_group(token):
        group = get_object_or_404(Group, token=token)
        group.save()
        return group



class Person(models.Model):
    # Definition der einzelnen Eingabefelder fÃ¼r Personen auf den Personenunterseiten
    name = models.CharField(max_length=64,
                            blank=False,
                            verbose_name='Name',
                            help_text="Anzeigename der Person")
    group = models.ForeignKey(Group,
                              verbose_name='Gruppe',
                              help_text="Zuordnung der Person zu einer Gruppe, kann nicht geaendert werden.")

    """
    generiert einen report, wie viel die Personen erhalten
    negative Betraege: die Person erhaelt Geld
    positiv Betrag: die Person schuldet Geld

    :returns report {name: value, name: value}
    """

    def person_cost_report(self):
        # Kosten + Personen der Gruppe auslesen
        groupexpenses = Expense.objects.filter(group=self.group)
        grouppersons = Person.objects.filter(group=self.group)

        # Dictionary mit allen Personen der Gruppe erstellen
        personsarray = {}

        for person in grouppersons:
            if person == self:
                continue
            personsarray[person.name] = 0

        # ALLE AUSGABEN der GRUPPPE
        for expense in groupexpenses:

            # BERECHNET DEN KOSTENANTEIL
            # TODO durch 0 eventuell moeglich
            cost = expense.cost / (expense.costPersons.count())

            # GEHT ALLE PERSONEN DER AUSGABE DURCH
            for p in expense.costPersons.all():
                # TODO TESTEN
                if self == expense.owner:
                    if p != self:
                        personsarray[p.name] -= cost
                        continue
                elif p == expense.owner:
                    continue
                elif p == self:
                    personsarray[expense.owner.name] += cost
        return personsarray

    report = property(person_cost_report)

    # Rueckgabewert bei aufruf des Objekts
    def __str__(self):  # __unicode__ on Python 2
        return self.name


class Expense(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='Eindeutige Identifikationsnummer'),
    name = models.CharField(max_length=64,
                            blank=False,
                            verbose_name='Name',
                            help_text="Name der Ausgabe.")
    description = models.CharField(max_length=256,
                                   blank=True,
                                   verbose_name='Beschreibung',
                                   help_text="Beschreibung der Ausgabe (optional)")
    owner = models.ForeignKey(Person,
                              related_name='costOwner',
                              verbose_name='Besitzer',
                              help_text='Wer hat das Geld ausgelegt?')
    group = models.ForeignKey(Group,
                              verbose_name='Gruppe',
                              help_text="Zuordnung der Ausgabe zu einer Gruppe, kann nicht geaendert werden.")
    createDate = models.DateField(default=timezone.now,
                                  verbose_name='Erstellungsdatum',
                                  help_text="Gibt an wann die Ausgabe erstellt wurde.")
    debitDate = models.DateField(blank=True,
                                 default=timezone.now,
                                 verbose_name='Datum der Zahlung')
    costPersons = models.ManyToManyField(Person,
                                         blank=False,
                                         verbose_name='Teilhaber',
                                         help_text="Personen auf die diese Ausgabe aufgeteilt wird.")
    cost = models.FloatField(blank=False,
                             verbose_name="Ausgabe",
                             help_text="Wert der Ausgabe")

    # Rueckgabewert bei aufruf des Objekts
    def __str__(self):  # __unicode__ on Python 2
        return self.id


class Report(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='Eindeutige Identifikationsnummer'),
    owner = models.ForeignKey(Person, verbose_name='Besitzer', related_name='report_cost_owner',
                              help_text='Wer hat das Geld ausgelegt?', blank=False)
    costPerson = models.ForeignKey(Person, verbose_name='Schuldner', related_name='report_cost_person',
                                   help_text='Wer ist der Schuldner?', blank=False)
    group = models.ForeignKey(Group, verbose_name='Gruppe',
                              help_text="Zuordnung der Ausgabe zu einer Gruppe, kann nicht geaendert werden.",
                              related_name='report_group', blank=False)
    expense = models.ForeignKey(Expense, blank=False)
    cost = models.FloatField(blank=False, verbose_name="Ausgabe", help_text="Wert der Ausgabe")
    payed = models.BooleanField(default=0, blank=False)

    def __str__(self):  # __unicode__ on Python 2
        return self.expense
