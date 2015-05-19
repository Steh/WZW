from django.test import TestCase
from wzw.functions import create_token
import re

class GroupTestCase(TestCase):
    def createTokenTest(self):
        """Test of creatingToken"""
        testToken = create_token()
        assert re.fullmatch("([0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4})", testToken)
