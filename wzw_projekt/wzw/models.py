from django.db import models
from functions import *

class Person(models.Model):
    name = models.CharField(
        max_length=64,
        blank=False,
    )

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=128, blank=True)
    token = models.CharField(max_length=19, editable=False, unique=True)
    lastLogon = models.DateField('Last Logon', auto_now=True, blank=False)

    def __str__(self):              # __unicode__ on Python 2
        return self.name

    def save(self, *args, **kwargs):
        if not self.pk:
            token_existing = True
            while token_existing:
                token = create_token()

                ## wenn gruppe existiert wird die schleife erneut ausgefuehrt
                ## wenn nicht wird ein fehler geworfen und die Variable auf False gesetzt
                try:
                    Group.objects.get(token=token)
                    token_existing = True
                except Group.DoesNotExist:
                    token_existing = False
            self.token = token

        super(Group, self).save(*args, **kwargs)

class Expenses(models.Model):
    name = models.CharField(max_length=64, blank=False)
    description = models.CharField(max_length=256, blank=True)
    owner = models.ForeignKey(Person, related_name='costOwner')
    group = models.ForeignKey(Group)
    createDate = models.DateField('date published')
    debitDate = models.DateField('date debited', blank=True)
    costPersons = models.ManyToManyField(Person, blank=True)
    cost = models.FloatField(blank=False)

    def __str__(self):              # __unicode__ on Python 2
        return self.name
