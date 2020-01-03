from django.test import TestCase
from .models import Strain

# Create your tests here.
class StrainTests(TestCase):

    def test_str(self):
        test_name = Strain(name='A strain')
        self.assertEqual(str(test_name), 'A strain')

