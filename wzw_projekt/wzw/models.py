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

    # override original save methode
    # if no primary key is available (only by new objects)
    # token will be generated
    def save(self, *args, **kwargs):
        if not self.pk:
            token = create_token()
            self.token = token

        super(Group, self).save(*args, **kwargs)

    # ueberschreibt die loeschen methode
    # dadurch werden auch alle kosten + personen geloescht
    def delete(self, using=None):
        # 1. loeschen aller Personen die zu dieser Gruppe gehoeren
        # 2. loeschen aller Personen die zu dieser Gruppe gehoeren
        # 3. loeschen der Gruppe

        person = Person.objects.filter(group=self)
        person.delete()

        expense = Expense.objects.filter(group=self)
        expense.delete()

        super(Group, self).delete()


class Person(models.Model):
    name = models.CharField(max_length=64, blank=False)
    group = models.ForeignKey(Group)

    def __str__(self):  # __unicode__ on Python 2
        return self.name


class Expense(models.Model):
    name = models.CharField(max_length=64, blank=False)
    description = models.CharField(max_length=256, blank=True)
    owner = models.ForeignKey(Person, related_name='costOwner')
    group = models.ForeignKey(Group)
    createDate = models.DateField('date published', default=timezone.now)
    debitDate = models.DateField('date debited', blank=True, default=timezone.now)
    costPersons = models.ManyToManyField(Person, blank=True, verbose_name='costPerson_PersonId')
    cost = models.FloatField(blank=False)

    def __str__(self):  # __unicode__ on Python 2
        return self.name
