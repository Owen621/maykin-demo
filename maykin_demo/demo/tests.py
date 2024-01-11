from django.test import TestCase
from .models import *
# Create your tests here.

class URLTests(TestCase):
    def testHome(self):
        response = self.client.get("/home")
        self.assertEqual(response.status_code, 200)


class TestModels(TestCase):

    def testStr(self):
        hotel = Hotel.objects.create(city=City.objects.create(
            cityName="testCity"),hotelName="test hotel")
        self.assertEqual(str(hotel), "test hotel")

    def testSlug(self):
        hotel = Hotel.objects.create(city=City.objects.create(
            cityName="testCity"), hotelCode="TESTcode123")
        hotel.save()
        self.assertEqual(hotel.slug, "testcode123")