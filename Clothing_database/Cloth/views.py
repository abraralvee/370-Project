from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import RenteeRegistrationForm, RenterRegistrationForm, DeliveryPersonRegistrationForm
from django.db import connection
from django.contrib import messages
# Assuming you have a custom user model
from .models import User

def register_rentee(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        address = request.POST['address']
        phone = request.POST['phone_number']
        password1 = request.POST['password']
        password2 = request.POST['confirm_password']
        NID = request.POST['nid']
        user_id= '02'+ str(NID)
        password = None

        if password1==password2:
            password = password1
        else:
            messages.warning(request, "Please retype the password properly")
            return redirect('../register_rentee')
    
        data = {
            'user_id': user_id,
            'user_name' : first_name +' '+ last_name,
            'user_email': email,
            'user_address': address
        }
        find_user = "select user_id from cloth_user"
        insert_user = 'insert into cloth_user (user_id, first_name, last_name, password, phone_number) values (%s, %s,%s, %s, %s)'
        insert_rentee = 'insert into cloth_rentee (User_ID_id, NID,  Shipping_address, email) values ( %s, %s, %s, %s) '

        with connection.cursor() as cursor:
            cursor.execute(find_user)
            user_list = tuple(cursor.fetchall())
            print(user_list)
            if user_id in user_list:
                messages.warning(request, 'You already have an account')
                return redirect('../login')
            else:
                cursor.execute(insert_user, (user_id, first_name, last_name, password, phone))


        with connection.cursor() as cursor:
            cursor.execute(find_user)
            user_list = tuple(cursor.fetchall())
            if user_id in user_list:
                messages.warning(request, 'You already have an account')
                return redirect('../login')
            else:
                cursor.execute(insert_rentee, (user_id, NID, address ,email))

        messages.success(request, 'Signup Successful')
        return render(request, 'rentee-dashboard.html', data)
    return render(request, 'register_rentee.html')

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
        print(user_id,SSN)

        if password1==password2:
            password = password1
            print(password)
        else:
            messages.warning(request, "Please retype the password properly")
            return redirect('../register_renter')
    
        data = {
            'user_id': user_id,
            'user_name' : first_name +' '+ last_name,
            'user_email': email,
            'user_address': address
        }

        find_user = "select user_id from cloth_user"
        insert_user = 'insert into cloth_user (user_id, first_name, last_name, password, phone_number) values (%s, %s,%s, %s, %s)'
        insert_renter = 'insert into cloth_renter (User_ID_id, SSN, Rating, address, email) values ( %s, %s, %s, %s, %s) '

        with connection.cursor() as cursor:
            cursor.execute(find_user)
            user_list = tuple(cursor.fetchall())
            print(user_list)
            if user_id in user_list:
                messages.warning(request, 'You already have an account')
                return redirect('../login')
            else:
                cursor.execute(insert_user, (user_id, first_name, last_name, password, phone))
        print(user_id, first_name)


        with connection.cursor() as cursor:
            cursor.execute(find_user)
            user_list = tuple(cursor.fetchall())
            if user_id in user_list:
                messages.warning(request, 'You already have an account')
                return redirect('../login')
            else:
                cursor.execute(insert_renter, (user_id, SSN, Rating, address ,email))

        messages.success(request, 'Signup Successful')
        return render(request, 'renter-dashboard.html', data)
    return render(request, 'register_renter.html')

def register_delivery_person(request):
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

        if password1==password2:
            password = password1
            print(password)
        else:
            messages.warning(request, "Please retype the password properly")
            return redirect('register_renter')
    
        # data = {
        #     'user_id': user_id,
        #     'user_name' : first_name + last_name,
        #     'user_email': email,
        #     'user_address': address
        # }
        find_user = "select user_id from cloth_user"
        insert_user = 'insert into cloth_user (user_id, first_name, last_name, password, phone_number) values (%s, %s,%s, %s, %s)'
        insert_renter = 'insert into cloth_renter (User_ID_id, SSN, Rating, address, email) values ( %s, %s, %s, %s, %s) '

        with connection.cursor() as cursor:
            cursor.execute(find_user)
            user_list = tuple(cursor.fetchall())
            print(user_list)
            if user_id in user_list:
                messages.warning(request, 'You already have an account')
                return render(request, 'login')
            else:
                cursor.execute(insert_user, (user_id, first_name, last_name, password, phone))


        with connection.cursor() as cursor:
            cursor.execute(find_user)
            user_list = tuple(cursor.fetchall())
            if user_id in user_list:
                messages.warning(request, 'You already have an account')
                return render(request, 'login')
            else:
                cursor.execute(insert_renter, (user_id, SSN, Rating, address ,email))

        messages.success(request, 'Signup Successful')
        # return render(request, 'user.html', data)
    return render(request, 'register_renter.html')

def home(request):
    return render(request, 'homepage.html')


def login_view(request):
    return render(request, 'login.html')

def renter_dashboard(request):
    return render(request, 'renter-dashboard.html')