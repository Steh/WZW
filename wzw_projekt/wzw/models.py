from django.db import models
from functions import create_token

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
    token = model.CharField(max_length=19, editable=False)
    lastLogon = models.DateField('Last Logon', auto_now=True, blank=False)
    email = models.EmailField(blank=True)
    pwd = models.CharField(max_length=32, blank=True)

    def __str__(self):              # __unicode__ on Python 2
        return self.name

    def save(self, *args, **kwargs):
        if self.pk:
            self.token = property(create_token())
         super(Post, self).save(*args, **kwargs)

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
