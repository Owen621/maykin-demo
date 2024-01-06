from django.shortcuts import render
from django.http import HttpResponse
from .models import Hotel, City

# Create your views here.

def home(request):

    citySelected = None
    hotels = []
    for city in City.objects.filter():
        if city.cityName in request.GET:
            citySelected = city
            break
    
    if citySelected != None:
        hotels = Hotel.objects.filter(city=citySelected)

        

    context = {"empty": ((len(Hotel.objects.filter()) == 0) 
                         or (len(City.objects.filter()) == 0)),
               "cities": City.objects.filter(),
               "citySelected": citySelected,
               "hotels": hotels}
    
    return render(request, 'demo/home.html', context)