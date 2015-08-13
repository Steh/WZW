# -*- coding: utf-8 -*-

import re

from django.test import TestCase

from wzw.models import Group, Person, Expense
from wzw.functions import create_token


class GroupTests(TestCase):
    def test_createGroup(self):
        """
        erstellt Gruppe mit und ohne name

        """
        Group.objects.create(name='test')
        Group.objects.create()

    def test_createToken(self):
        """Test of creatingToken"""
        token = create_token()
        self.assertTrue(re.match("^([0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}$)", token))


class PersonTests(TestCase):

    def setUp(self):
        Group.objects.create(name='Gruppe')
        Group.objects.create(name='Gruppe2')

    def test_createPerson(self):
        '''
        Person erstellen
        testen ob Name und Gruppe richtig sind
        '''
        group = Group.objects.get(name='Gruppe')
        p1 = Person.objects.create(name='Stefan', group=group)
        self.assertEquals(p1.name, 'Stefan')
        self.assertEquals(p1.group, group)

    def test_personGroup(self):
        '''
        testen ob Personen den Gruppen zugeordnet werden konnten
        '''
        group1 = Group.objects.get(name='Gruppe')
        group2 = Group.objects.get(name='Gruppe2')

        Person.objects.create(name='Stefan', group=group1)
        Person.objects.create(name='Stefan2', group=group1)
        Person.objects.create(name='Stefan', group=group2)

        self.assertEquals(Person.objects.filter(group=group1).count(), 2)
        self.assertEquals(Person.objects.filter(group=group2).count(), 1)


class ReportTests(TestCase):
    def test_Report_Even(self):
        """
        ES WIRD EINE GRUPPE MIT DREI PERSONEN ANGELEGT
        Jeder Bezahlt eine Rechnung für DREI LEUTE
        AM ENDE MUSS ES SICH AUSGLEICHEN
        """
        group = Group.objects.create()
        p1 = Person.objects.create(name='p1', group=group)
        p2 = Person.objects.create(name='p2', group=group)
        p3 = Person.objects.create(name='p3', group=group)

        for key, value in p1.report.items() and p2.report.items() and p3.report.items():
            self.assertEqual(value, 0, 'Report muss leer sein, solange noch keine Ausgaben erstellt wurden')

        e1 = Expense.objects.create(name='Ausgabe1', group=group, owner=p1, cost='30')
        e1.costPersons.add(p1)
        e1.costPersons.add(p2)
        e1.costPersons.add(p3)
        # TODO self.assertEqual(p1.report, '{u'p2': 10.0, u'p3': 10.0}', p1.report)

        e2 = Expense.objects.create(name='Ausgabe2', group=group, owner=p2, cost='30')
        e2.costPersons.add(p1)
        e2.costPersons.add(p2)
        e2.costPersons.add(p3)
        # TODO self.assertEqual(p1.report, '{u'p2': 0.0, u'p3': 10.0}', p1.report)

        e3 = Expense.objects.create(name='Ausgabe3', group=group, owner=p3, cost='30')
        e3.costPersons.add(p1)
        e3.costPersons.add(p2)
        e3.costPersons.add(p3)

        for key, value in p1.report.items() and p2.report.items() and p3.report.items():
            self.assertEqual(value, 0, 'Report muss leer sein, Ausgaben gleichen sich aus')
