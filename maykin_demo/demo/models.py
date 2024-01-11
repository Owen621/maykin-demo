from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
# Create your models here.

class City (models.Model):

    cityCode = models.CharField(max_length=3)
    cityName = models.CharField(max_length=255)

    #useful for displaying the actual city names on the forms
    #rather than city object (1) etc
    def __str__(self):
        return self.cityName

class Hotel (models.Model):

    #slug field used so each hotel can have a page to be edited
    slug = models.SlugField(max_length=100, unique=True)
    city = models.ForeignKey(
        City, blank=True, on_delete=models.CASCADE)
    hotelCode = models.CharField(max_length=10)
    hotelName = models.CharField(max_length=255)

    def __str__(self):
        return self.hotelName
    
    #save the slug field
    def save(self, *args, **kwargs):
        value = self.hotelCode
        self.slug = slugify(value)
        super().save(*args, **kwargs)




class ExtendedUser(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #on_delete=models.SET_NULL is used so that users are not deleted if the city
    #is. The user will be asked to select a new city however.
    city = models.ForeignKey(
        City, null=True, on_delete=models.SET_NULL)
