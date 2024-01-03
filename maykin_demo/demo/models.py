from django.db import models

# Create your models here.

class City (models.Model):

    cityCode = models.CharField(max_length=3)
    cityName = models.CharField(max_length=255)

class Hotel (models.Model):

    city = models.ForeignKey(
        City, blank=True, on_delete=models.CASCADE)
    hotelCode = models.CharField(max_length=10)
    hotelName = models.CharField(max_length=255)
