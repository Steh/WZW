import re

from django.test import TestCase

from wzw.models import Group
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