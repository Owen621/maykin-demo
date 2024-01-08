from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Hotel, City
from .forms import RegisterForm, ExtendedUserForm
from django.contrib.auth import login, authenticate
from .decorators import authenticated_user, unauthenticated_user

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


@unauthenticated_user
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        extended_form = ExtendedUserForm(response.POST)
        if form.is_valid() and extended_form.is_valid():
            user = form.save()
            extendedUserInstance = extended_form.save(commit=False)
            extendedUserInstance.user = user
            extendedUserInstance.save()
            return redirect("/login")
        else:
            pass
    else:
        form = RegisterForm()
        extended_form = ExtendedUserForm()
    context = {'form' : form, 'extended_form':extended_form}
    return render(response, "demo/register.html", context)


@unauthenticated_user
def Userlogin(response):

    failed = False
    if "failed" in response.GET:
        failed = True

    if response.method == "POST":
        username = response.POST.get('username')
        password = response.POST.get('password')

        user = authenticate(response, username=username, password=password)
        if user is not None:
            login(response, user)
            return redirect('/edit')
        else:
            return redirect("/login?failed")

    return render(response, "demo/login.html", {"failed":failed})


@authenticated_user
def edit(response):

    context = {}
    return render(response, "demo/edit.html", context)
