from django.test import TestCase

# Create your tests here.
class PageTesting(TestCase):

    def home_page_test(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)