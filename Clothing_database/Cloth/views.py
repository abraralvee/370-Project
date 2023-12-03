from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .forms import RenteeRegistrationForm, RenterRegistrationForm, DeliveryPersonRegistrationForm

# Assuming you have a custom user model
from .models import User

def register_rentee(request):
    if request.method == 'POST':
        form = RenteeRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.Role = '01'
            user.save()

            # Log in the user after registration
            login(request, user)

            return redirect('success_page')  # Redirect to a success page
    else:
        form = RenteeRegistrationForm()
    return render(request, 'register_rentee.html', {'form': form})

def register_renter(request):
    if request.method == 'POST':
        form = RenterRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.Role = '02'
            user.save()

            # Log in the user after registration
            login(request, user)

            return redirect('success_page')  # Redirect to a success page
    else:
        form = RenterRegistrationForm()
    return render(request, 'register_renter.html', {'form': form})

def register_delivery_person(request):
    if request.method == 'POST':
        form = DeliveryPersonRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.Role = '03'
            user.save()

            # Log in the user after registration
            login(request, user)

            return redirect('success_page')  # Redirect to a success page
    else:
        form = DeliveryPersonRegistrationForm()
    return render(request, 'register_delivery_person.html', {'form': form})

def home(request):
    return render(request, 'homepage.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('index')  # Change 'index' to the name of your home page URL
        else:
            # Return an 'invalid login' error message.
            return render(request, 'login.html', {'error': 'Invalid login credentials'})

    return render(request, 'login.html')