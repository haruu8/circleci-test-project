from django.test import TestCase
from .views import SampleView

class SampleViewTestCase(TestCase):
    def test_sample(self):
        client = self.client
        response = client.get('/')
        self.assertEqual(response.status_code, 404)
