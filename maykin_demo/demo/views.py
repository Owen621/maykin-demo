from django.shortcuts import render
from django.http import HttpResponse
from .forms import CsvModelForm
from .models import Csv
# Create your views here.

def home(request):


    context = {}
    return render(request, 'demo/home.html', context)