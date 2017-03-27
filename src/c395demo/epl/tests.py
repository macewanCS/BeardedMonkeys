from django.test import TestCase
from epl.models import CallLog

# Create your tests here.

class CallLogTestCase(TestCase):
    def test_login(self):
        ''' Testing for Login Page '''
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)
