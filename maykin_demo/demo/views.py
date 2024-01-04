from django.shortcuts import render
from django.http import HttpResponse
from .models import Hotel, City

# Create your views here.

def home(request):

    context = {"empty": ((len(Hotel.objects.filter()) == 0) 
                         or (len(City.objects.filter()) == 0))}
    return render(request, 'demo/home.html', context)