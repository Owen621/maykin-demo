import csv
from demo.models import Hotel, City
from django.core.management.base import BaseCommand
from demo.forms import CityForm, HotelForm

class Command(BaseCommand):


    def handle(self, *args, **kwargs):
        pass
    def importCities(file_path):
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                City.objects.create(
                    cityCode=row[0],
                    CityName=row[1],
                )

    def importHotels(file_path):
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                Hotel.objects.create(
                    city=City.objects.filter(cityCode=row[0]),
                    hotelCode=row[1],
                    hotelName=row[2]
                )
