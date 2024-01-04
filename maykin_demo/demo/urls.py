from .views import home
from django.urls import path

app_name = 'demo'

urlpatterns = [
    path('', home, name="home-view"),
]