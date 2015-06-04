from django.utils import timezone
from django.db import models

from wzw.functions import create_token

class Group(models.Model):
    name = models.CharField(max_length=32,
                            blank=True,
                            default='',
                            verbose_name="Gruppenname",
                            help_text="Name fuer die Gruppe (optional)")
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

    # Rueckgabewert bei aufruf des Objekts
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


class Person(models.Model):
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
    def personcostreport(self):
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

    report = property(personcostreport)

    # Rueckgabewert bei aufruf des Objekts
    def __str__(self):  # __unicode__ on Python 2
        return self.name


class Expense(models.Model):
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
                                  verbose_name='Erstellungs Datum',
                                  help_text="Gibt an wann die Ausgabe erstellt wurde.")
    debitDate = models.DateField(blank=True,
                                 default=timezone.now,
                                 verbose_name='',
                                 help_text="Gibt an wann die Ausgabe bezahlt wurde.")
    costPersons = models.ManyToManyField(Person,
                                         blank=False,
                                         verbose_name='Teilhaber',
                                         help_text="Personen auf die diese Ausgabe aufgeteilt wird.")
    cost = models.FloatField(blank=False,
                             verbose_name="Ausgabe",
                             help_text="Wert der Ausgabe")

    # Rueckgabewert bei aufruf des Objekts
    def __str__(self):  # __unicode__ on Python 2
        return self.name
