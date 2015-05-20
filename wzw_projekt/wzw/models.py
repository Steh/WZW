from django.db import models
from wzw.functions import create_token

class Person(models.Model):
    name = models.CharField(max_length=64,blank=False)

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=128, blank=True)
    token = models.CharField(max_length=19, editable=False, unique=True)
    lastLogon = models.DateField('Last Logon', auto_now=True, blank=False)

    def __str__(self):              # __unicode__ on Python 2
        return self.token

    # override original save methode
    #     if no primary key is available (only by new objects)
    #     token will be generated
    def save(self, *args, **kwargs):
        if not self.pk:
            token = create_token()
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
