import csv
from demo.models import Hotel, City
import requests
from django.core.management.base import BaseCommand
from requests.auth import HTTPBasicAuth

#I cannot use django-cron in windows
class Command(BaseCommand):

    help = ("Imports data on hotels and cities over authenticated HTTP into hotel and city models respetively")

    def handle(self, *args, **kwargs):

        print("Starting import")
        self.main()
    
    def main(self):
        
        '''
        At first I assumed that this command will be overwriting the previous
        data everyday. However this approach does not make sense for the
        further bullet points in the task, due to the fact that Users are
        created who can add, update and delete these hotels. This means that
        this command will essentially overwrite all their work as well as
        disrupting the relation between extended user and city, and so I have
        adapted it to only add new records into the database. It is only a small
        change and can easily be reverted anyway.
        '''

        csv_city = 'http://rachel.maykinmedia.nl/djangocase/city.csv'
        csv_hotel = 'http://rachel.maykinmedia.nl/djangocase/hotel.csv'
        details = HTTPBasicAuth('python-demo', 'claw30_bumps')
        response = [
            requests.get(csv_city, auth=details),
            requests.get(csv_hotel, auth=details),
            ]
        
        
        reader = csv.reader(response[0].text.splitlines(), delimiter=';')
        for row in reader:
            #if this city does not already exist in the database
            if len(City.objects.filter(cityCode=row[0])) == 0:
                City.objects.create(
                    cityCode=row[0],
                    cityName=row[1],
                )

    
        reader = csv.reader(response[1].text.splitlines(), delimiter=';')
        for row in reader:
            if len(Hotel.objects.filter(hotelCode=row[1])) == 0:
                Hotel.objects.create(
                    city=City.objects.get(cityCode=row[0]),
                    hotelCode=row[1],
                    hotelName=row[2]
                )
        print("Done")
