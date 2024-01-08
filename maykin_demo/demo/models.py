from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class City (models.Model):

    cityCode = models.CharField(max_length=3)
    cityName = models.CharField(max_length=255)

    def __str__(self):
        return self.cityName

class Hotel (models.Model):

    city = models.ForeignKey(
        City, blank=True, on_delete=models.CASCADE)
    hotelCode = models.CharField(max_length=10)
    hotelName = models.CharField(max_length=255)


class ExtendedUser(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.ForeignKey(
        City, blank=False, on_delete=models.CASCADE)
    