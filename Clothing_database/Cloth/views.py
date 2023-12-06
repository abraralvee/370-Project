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
            return redirect('register_rentee')
    
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
                    return redirect('login')
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
            return redirect('register_renter')
    
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
                    return redirect('login')
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
                    return redirect('login')
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
    data_info = {}

    if request.method == "POST":
        key = request.POST['key']
        user = request.POST['user_type']
        user_id = None

        if user == "renter":
            user_id = '01' + str(key)
            info_query = "SELECT * FROM cloth_renter WHERE User_ID_id = %s"
        elif user == "rentee":
            user_id = '02' + str(key)
            info_query = "SELECT * FROM cloth_rentee WHERE User_ID_id = %s"
        elif user == "dp":
            user_id = '03' + str(key)
            info_query = "SELECT * FROM cloth_delivery_person WHERE User_ID_id = %s"

        info= "SELECT * FROM cloth_user WHERE User_ID = %s"

        with connection.cursor() as cursor:
            cursor.execute(info, [user_id])
            data= cursor.fetchone()

        data_info.update({
                'user_id' : data[0],
                'user_name' : data[1]+ ' ' + data[2],
                'phone_number': data[4]
            })

        retrieve_pass = "SELECT password FROM cloth_user WHERE User_ID = %s"

        with connection.cursor() as cursor:
            # Fetch user-specific data
            cursor.execute(info_query, [user_id])
            user_data = cursor.fetchone()

            if user_data:
                # Update data_info based on user type
                if user == "renter":
                    data_info.update({
                        'user_rating': user_data[2],
                        'user_address': user_data[3],
                        'user_email': user_data[4]
                    })
                elif user == "rentee":
                    data_info.update({
                        'user_address': user_data[2],
                        'user_email': user_data[3]
                    })
                elif user == "dp":
                    data_info.update({
                        'user_serial': user_data[1]
                    })

                # Check password and render view
                password = request.POST['password']
                cursor.execute(retrieve_pass, [user_id])
                pass_info = cursor.fetchone()

                if pass_info and pass_info[0] == password:
                    return render(request, f'{user}-dashboard.html', data_info)
                else:
                    messages.warning(request, "Wrong password")
                    return redirect('login')

    return render(request, 'login.html')


def login(request):
    return render(request, 'login.html')
def renter_dashboard(request):
    return render(request, 'renter-dashboard.html')
def rentee_dashboard(request):
    return render(request, 'rentee-dashboard.html')
def dp_dashboard(request):
    return render(request, 'dp-dashboard.html')