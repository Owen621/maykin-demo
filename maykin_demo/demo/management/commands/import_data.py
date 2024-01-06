import csv
from demo.models import Hotel, City
import requests
from django.core.management.base import BaseCommand
from requests.auth import HTTPBasicAuth

class Command(BaseCommand):

    help = ("Imports data on hotels and cities over authenticated HTTP into hotel and city models respetively")

    def handle(self, *args, **kwargs):

        print("Starting import")
        self.main()
    
    def main(self):

        City.objects.all().delete()
        Hotel.objects.all().delete()
        
        csv_city = 'http://rachel.maykinmedia.nl/djangocase/city.csv'
        csv_hotel = 'http://rachel.maykinmedia.nl/djangocase/hotel.csv'
        details = HTTPBasicAuth('python-demo', 'claw30_bumps')
        response = [
            requests.get(csv_city, auth=details),
            requests.get(csv_hotel, auth=details),
            ]
        
        
        reader = csv.reader(response[0].text.splitlines(), delimiter=';')
        for row in reader:
            City.objects.create(
                cityCode=row[0],
                cityName=row[1],
            )

    
        reader = csv.reader(response[1].text.splitlines(), delimiter=';')
        for row in reader:
            Hotel.objects.create(
                city=City.objects.get(cityCode=row[0]),
                hotelCode=row[1],
                hotelName=row[2]
            )
        print("Done")
