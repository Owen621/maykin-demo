from .views import home
from django.urls import path

app_name = 'demo'

urlpatterns = [
    path('home', home, name="home-view"),
]