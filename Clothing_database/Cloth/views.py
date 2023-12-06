from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.contrib import messages
from django.db import connection

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
        find_user = "SELECT user_id FROM cloth_user WHERE user_id = %s"
        insert_user = 'insert into cloth_user (user_id, first_name, last_name, password, phone_number) values (%s, %s,%s, %s, %s)'
        insert_rentee = 'insert into cloth_rentee (User_ID_id, NID,  Shipping_address, email) values ( %s, %s, %s, %s) '

        with connection.cursor() as cursor:
                cursor.execute(find_user, (user_id,))
                existing_user = cursor.fetchone()
                if existing_user:
                    messages.warning(request, 'You already have an account')
                    return redirect('../login')
                else:
                    cursor.execute(insert_user, (user_id, first_name, last_name, password, phone))
                    cursor.execute(insert_rentee, (user_id, NID, address, email))
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

        if password1==password2:
            password = password1
        else:
            messages.warning(request, "Please retype the password properly")
            return redirect('../register_renter')
    
        data = {
            'user_id': user_id,
            'user_name' : first_name +' '+ last_name,
            'user_email': email,
            'user_address': address
        }

        find_user = "SELECT user_id FROM cloth_user WHERE user_id = %s"
        insert_user = 'INSERT INTO cloth_user (user_id, first_name, last_name, password, phone_number) VALUES (%s, %s, %s, %s, %s)'
        insert_renter = 'INSERT INTO cloth_renter (User_ID_id, SSN, Rating, address, email) VALUES (%s, %s, %s, %s, %s)'

        with connection.cursor() as cursor:
                cursor.execute(find_user, (user_id,))
                existing_user = cursor.fetchone()
                if existing_user:
                    messages.warning(request, 'You already have an account')
                    return redirect('../login')
                else:
                    cursor.execute(insert_user, (user_id, first_name, last_name, password, phone))
                    cursor.execute(insert_renter, (user_id, SSN, Rating, address, email))
                    messages.success(request, 'Signup Successful')
                    return render(request, 'renter-dashboard.html', data)
                
    return render(request, 'register_renter.html')

def register_delivery_person(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone = request.POST['phone_number']
        password1 = request.POST['password']
        password2 = request.POST['confirm_password']
        SSN = request.POST['ssn']
        user_id= '03'+ str(SSN)
        password = None

        if password1==password2:
            password = password1
        else:
            messages.warning(request, "Please retype the password properly")
            return redirect('../register_dp')
    
        data = {
            'user_id': user_id,
            'user_name' : first_name + ' ' + last_name,
        }

        find_user = "SELECT user_id FROM cloth_user WHERE user_id = %s"
        insert_user = 'insert into cloth_user (user_id, first_name, last_name, password, phone_number) values (%s, %s,%s, %s, %s)'
        insert_dp = 'insert into cloth_delivery_person (User_ID_id, SSN) values ( %s, %s) '

        with connection.cursor() as cursor:
                cursor.execute(find_user, (user_id,))
                existing_user = cursor.fetchone()
                if existing_user:
                    messages.warning(request, 'You already have an account')
                    return redirect('../login')
                else:
                    cursor.execute(insert_user, (user_id, first_name, last_name, password, phone))
                    cursor.execute(insert_dp, (user_id, SSN))
                    messages.success(request, 'Signup Successful')
                    return render(request, 'dp-dashboard.html', data)
                
    return render(request, 'register_dp.html')

def home(request):
    return render(request, 'homepage.html')


from django.urls import reverse

def login_view(request):
    key = None
    password = None

    if request.method == "POST":
        key = request.POST['key']
        user = request.POST['user_type']

        if user == "renter":
            user_id = '01' + str(key)
        elif user == "rentee":
            user_id = '02' + str(key)
        elif user == "dp":
            user_id = '03' + str(key)

        retrieve_pass = "SELECT password FROM cloth_user WHERE user_id = %s"
        retrieve_name = "SELECT user_id FROM cloth_user WHERE user_id = %s"

        password = request.POST['password']
        pass_info = ""
        id_info = ""

        with connection.cursor() as cursor:
            cursor.execute(retrieve_pass, [user_id])
            pass_info = cursor.fetchone()
            print(pass_info)

            if pass_info and pass_info[0] == password:
                cursor.execute(retrieve_name, [user_id])
                id_info = cursor.fetchone()[0]

                # dashboard_url = reverse(f'../{user}-dashboard')
                return redirect((f'../{user}-dashboard'), user_id)
            else:
                messages.warning(request, "Wrong password")
                return redirect('../login')

    return render(request, 'login.html')

def renter_dashboard(request):
    return render(request, 'renter-dashboard.html')
def rentee_dashboard(request):
    return render(request, 'rentee-dashboard.html')
def dp_dashboard(request):
    return render(request, 'dp-dashboard.html')