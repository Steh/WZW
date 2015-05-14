from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=64)

    @property
    def __unicode__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=128)
    lastLogon = models.DateField('date logon')
    email = models.EmailField()

    @property
    def __unicode__(self):
        return self.name


class Expenses(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    owner = models.ForeignKey(Person)
    group = models.ForeignKey(Group)
    createDate = models.DateTimeField('date published')
    debitDate = models.DateTimeField('date debited')
    costPersons = models.ManyToManyRel(Person)
    cost = models.FloatField()

    @property
    def __unicode__(self):
        return self.name