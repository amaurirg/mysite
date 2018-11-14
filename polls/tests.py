from django.http import HttpResponse
from django.test import TestCase


class IndexTest(TestCase):
    def test_view_index(self):
        """ Verify view index exist """
        url = 'http://localhost:8000/index'
