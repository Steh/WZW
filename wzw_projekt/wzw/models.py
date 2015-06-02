from django.utils import timezone
from django.db import models

from wzw.functions import create_token


class Group(models.Model):
    name = models.CharField(max_length=32, blank=True, default='')
    description = models.CharField(max_length=128, blank=True, default='')
    token = models.CharField(max_length=19, editable=False, unique=True)
    lastLogon = models.DateField('Last Logon', auto_now=True, blank=False)

    def __str__(self):  # __unicode__ on Python 2
        return self.token

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
    '''
    def delete(self, using=None):
        person = Person.objects.filter(group=self)
        person.delete()

        expense = Expense.objects.filter(group=self)
        expense.delete()

        super(Group, self).delete()


class Person(models.Model):
    name = models.CharField(max_length=64, blank=False)
    group = models.ForeignKey(Group)

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

    def __str__(self):  # __unicode__ on Python 2
        return self.name


class Expense(models.Model):
    name = models.CharField(max_length=64, blank=False)
    description = models.CharField(max_length=256, blank=True)
    owner = models.ForeignKey(Person, related_name='costOwner')
    group = models.ForeignKey(Group)
    createDate = models.DateField('date published', default=timezone.now)
    debitDate = models.DateField('date debited', blank=True, default=timezone.now)
    costPersons = models.ManyToManyField(Person, blank=False, verbose_name='costPerson_PersonId')
    cost = models.FloatField(blank=False)

    def __str__(self):  # __unicode__ on Python 2
        return self.name
