from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
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
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        address = request.POST['address']
        phone = request.POST['phone_number']
        password1 = request.POST['password']
        password2 = request.POST['confirm_password']
        SSN = request.POST['ssn']
        user_id= '01'+ str(SSN)
        Rating= None
        password = None
        print(user_id, first_name, last_name, password, phone)

        if password1==password2:
            password = password1
        else:
            messages.warning(request, "Please retype the password properly")
            return redirect('../register_renter.html/')
    
        data = {
            'user_id': user_id,
            'user_name' : first_name + last_name,
            'user_email': email,
            'user_address': address
        }
        insert_user = 'insert into cloth_user (user_id, first_name, last_name, password, phone_number) values (%s, %s,%s, %s, %s)'
        insert_renter = 'insert into cloth_renter ( SSN, Rating, address, email) values ( %s, %s, %s, %s) '
        with connection.cursor() as cursor:
            
            cursor.execute(insert_user, (user_id, first_name, last_name, password, phone))
            cursor.execute(insert_renter, (user_id, SSN, Rating, address ,email))
        print(user_id,SSN)
        messages.success(request, 'Signup Successful')
        return render(request, 'user.html', data)
    # print(user_id, first_name, last_name, password, phone)
    return render(request, 'register_renter.html')

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