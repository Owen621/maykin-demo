import csv
from demo.models import Hotel, City
from django.core.managenent.base import BaseCommand

class Command(BaseCommand):

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

    if __name__ == '__main__':
        csv_city_file_path = 'city.csv'
        csv_hotel_file_path = 'hotel.csv'
        importCities(csv_city_file_path)
        importHotels(csv_hotel_file_path)