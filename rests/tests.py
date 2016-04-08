from django.test import TestCase
from .models import Restaurant
from django.core.urlresolvers import reverse
from django.utils import timezone

class RestTestCase(TestCase):
    def setUp(self):
        rest1 = Restaurant.objects.create(name="pizza", address="seoul",rating=5, phone_number="0221945000", image="http://www.google.com",price="20")
        rest2 = Restaurant.objects.create(name="chicken", address="busan",rating=5, phone_number="0621945000", image="http://www.google.com",price="10")

    def test_rest_have_name(self):
        """Rests Test
            Fields tested : name,address,rating,createdAt
        """
        rest1 = Restaurant.objects.get(address="seoul")
        rest2 = Restaurant.objects.get(address="busan")
        self.assertEqual(rest1.name, 'pizza')
        self.assertEqual(rest1.rating, 5)
        self.assertEqual(rest2.price, '10')
        self.assertEqual(rest2.name, 'chicken')

# class RestViewTests(TestCase):
#     def test_hack_index_page(self):
#         response = self.client.get(reverse('rest:rest_list'))
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response,'No posts available')
