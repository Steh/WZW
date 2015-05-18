from django.db import models
import string, random

# Create your models here.

class Person(models.Model):
    name = models.CharField(
        max_length=64,
        blank=False,
    )

    def __str__(self):              # __unicode__ on Python 2
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=128, blank=False)
    lastLogon = models.DateField('Last Logon', auto_now=True, blank=False)
    email = models.EmailField(blank=True)
    pwd = models.CharField(max_length=32, blank=True)

    def __str__(self):              # __unicode__ on Python 2
        return self.name

    def create_token():
        token = ''
        for x in range(0, 4):
            token += ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(4))
            if x <= 2:
                token += '-'

        return token

    token = property(create_token())



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
