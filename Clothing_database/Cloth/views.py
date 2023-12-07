from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .forms import RenteeRegistrationForm, RenterRegistrationForm, DeliveryPersonRegistrationForm
from django.db import connection
from django.contrib import messages
# Assuming you have a custom user model
from .models import User

# def register_rentee(request):
#     if request.method == 'POST':
#         form = RenteeRegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.Role = '01'
#             user.save()

#             # Log in the user after registration
#             login(request, user)

#             return redirect('success_page')  # Redirect to a success page
#     else:
#         form = RenteeRegistrationForm()
#     return render(request, 'register_rentee.html', {'form': form})

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


def renter_login_view(request):
    return render(request, 'renter_login.html')

def rentee_login_view(request):
    return render(request, 'rentee_login.html')

def renter_dashboard(request):
    return render(request, 'renter-dashboard.html')

def rentee_home(request):
    return render(request,'rentee_home.html')

def cart(request):
    return render (request,'cart.html')

def checkout(request):
    return render(request, 'credit_card.html')

def payment_method(request):
    return render(request, 'transaction.html')

def order_placed(request):
    return render(request, 'order_placed.html')

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