from .views import home, register, Userlogin, edit, deleteHotel, hotelPage, add
from django.urls import path

app_name = 'demo'

urlpatterns = [
    path('home', home, name="home-view"),
    path('register', register, name="register-view"),
    path('login', Userlogin, name="login-view"),
    path('edit', edit, name="edit-view"),
    path('delete/<int:pk>', deleteHotel, name="delete-view"),
    path('add', add, name="add"),
    path("<slug:slug>", hotelPage, name="hotel-view"),

]