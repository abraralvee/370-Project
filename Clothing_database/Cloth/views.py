from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .forms import RenteeRegistrationForm, RenterRegistrationForm, DeliveryPersonRegistrationForm
from django.db import connection
from django.contrib import messages
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
    if request.method == "POST":
        form = RenterRegistrationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.Role = '02'
            user.save()

            # Now you can access user attributes like user.user_id, user.first_name, etc.

            insert_renter = """
                INSERT INTO Renter (user_id, SSN, Rating, address, email)
                VALUES (%s, %s, %s, %s, %s)
            """

            with connection.cursor() as cursor:
                cursor.execute(insert_renter, (user.user_id, form.cleaned_data['SSN'], None, form.cleaned_data['address'], form.cleaned_data['email']))
            print(SSN)
            messages.success(request, 'Signup Successful')
            return redirect('../')  # Redirect to the user's profile page or any other desired page
        else:
            messages.warning(request, 'Please fix the errors in the form.')

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
    return render(request, 'login.html')

def renter_dashboard(request):
    return render(request, 'renter-dashboard.html')