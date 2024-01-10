from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Hotel, City, ExtendedUser
from .forms import RegisterForm, ExtendedUserForm, NewHotelForm, UpdateHotelForm
from django.contrib.auth import login, authenticate
from .decorators import authenticated_user, unauthenticated_user
from django.http import Http404

# Create your views here.

def home(request):

    citySelected = None
    hotels = []
    #finds the relevant city
    for city in City.objects.filter():
        if city.cityName in request.GET:
            citySelected = city
            break
    
    #orders the hotels to be displayed
    if citySelected != None:
        hotels = Hotel.objects.filter(city=citySelected).order_by("hotelCode")


    context = {"empty": ((len(Hotel.objects.filter()) == 0) 
                         or (len(City.objects.filter()) == 0)),
               "cities": City.objects.filter().order_by("cityName"),
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
            #commit=False used to return the instance and not yet save to database
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
        #the credentials are correct
        if user is not None:
            login(response, user)
            return redirect('/edit')
        else:
            return redirect("/login?failed")

    return render(response, "demo/login.html", {"failed":failed})


@authenticated_user
def edit(response):

    updated = False
    added = False
    deleted = False
    noCity = False
    form = None
    hotels = []

    #form for city has been submitted by user so extended user instance is updated
    if response.method == "POST":
        form = ExtendedUserForm(
            response.POST, instance=ExtendedUser.objects.get(user=response.user.id))
        if form.is_valid():
            form.save()
    else:

        if 'deleted' in response.GET:
            deleted = True 
        elif 'added' in response.GET:
            added = True
        elif 'updated' in response.GET:
            updated = True

        #the current user has no city so display the form
        if ExtendedUser.objects.get(user=response.user.id).city == None:
            form = ExtendedUserForm()
            noCity = True
        else:
            #all hotels in the current users city
            hotels = Hotel.objects.filter(city=ExtendedUser.objects.get(
                user=response.user.id).city).order_by("hotelCode")
    
        
    context = {"form": form, "noCity": noCity, "hotels": hotels,
                "deleted": deleted, "added": added, "updated": updated}
    return render(response, "demo/edit.html", context)

#view is actioned as a POST request from other views to delete hotel object
def deleteHotel(response, pk):
    try:
        hotel = Hotel.objects.get(id=pk)
    except:
        return redirect("/edit")
    
    if ExtendedUser.objects.get(user=response.user.id).city != hotel.city:
        return redirect("/edit")
        
    if response.method == "POST":
        hotel.delete()
        return redirect("/edit?deleted")
    
    else:
        return redirect("/edit")


@authenticated_user
def hotelPage(response, slug=None):

    hotel = None
    if slug is not None:
        try:
            hotel = Hotel.objects.get(slug=slug)
        except Hotel.DoesNotExist:
            raise Http404
        except Hotel.MultipleObjectsReturned:
           hotel = Hotel.objects.filter(slug=slug).first()
        except:
            raise Http404  
    
    #users assinged to different cities can only access those hotels
    if ExtendedUser.objects.get(user=response.user.id).city != hotel.city:
        return redirect("/home")
    else:
        if response.method == "POST":
            #pass in instance so that the record is updated rather than a new one created
            form = UpdateHotelForm(response.POST, instance=hotel)
            if form.is_valid():
                form.save()
                return redirect("/edit?updated")
        else:
            form = UpdateHotelForm()


    context = {"hotel": hotel, "form": form}

    return render(response, "demo/hotel.html", context)

@authenticated_user
def add(response):

    city = ExtendedUser.objects.get(user=response.user.id).city
    invalid = False
    exist = False

    if response.method == "POST":

        form = NewHotelForm(response.POST)
        if form.is_valid():
            #commit=false to change some more fields before saved
            hotel = form.save(commit=False)
            
            #the city code is the same as the beginning of the hotel code
            if city.cityCode.lower() == hotel.hotelCode.lower()[:len(city.cityCode)]:
                try:
                    #the rest of the string is numbers
                    int(hotel.hotelCode[len(city.cityCode):])
                    #no hotel exists with the same code
                    if len(Hotel.objects.filter(hotelCode=hotel.hotelCode.upper()))==0:
                        hotel.hotelCode = hotel.hotelCode.upper()
                        hotel.city = city
                        hotel.save()
                        return redirect("/edit?added")
                    else:
                        exist = True
                except ValueError:
                    invalid = True
            else:
                invalid = True
    else:
        form = NewHotelForm()
    
    context = {"form": form, "city": city, "invalid": invalid, "exist": exist}
    return render(response, "demo/add.html", context)
            