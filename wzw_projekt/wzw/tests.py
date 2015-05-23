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


class FormTests(TestCase):
    def setUp(self):
        nameGruppe = 'Test Gruppe'
        group = Group.objects.create(name=nameGruppe)
        person1 = Person.objects.create(name='person1', group=group)
        person2 = Person.objects.create(name='person2', group=group)
        expense = Expense.objects.create(name='ausgabe', owner=person1, group=group, cost='4.5')
        expense.costPersons.add(person1, person2)
        expense.save()
