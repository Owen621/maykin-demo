from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import ExtendedUser, Hotel
from django.forms import ModelForm

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]

class ExtendedUserForm(ModelForm):

    class Meta:
        model = ExtendedUser
        fields = ['city']

class UpdateHotelForm(ModelForm):

    class Meta:
        model = Hotel
        fields = ['hotelName']

class NewHotelForm(ModelForm):

    class Meta:
        model = Hotel
        fields = ['hotelCode', 'hotelName']