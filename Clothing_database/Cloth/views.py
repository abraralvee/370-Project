from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.contrib import messages
from django.db import connection
from django.core.files.storage import default_storage
from .models import ClothingItem  # Import your model

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
                    return render(request, 'login.html')
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
            return redirect('register_dp')
    
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

def login_view(request):
    key = request.POST.get('key')
    user_type = request.POST.get('user_type')
    password = request.POST.get('password')

    if not key or not user_type or not password:
        messages.warning(request, "Please provide all required information.")
        return redirect('login')

    user_id = f'01{key}' if user_type == 'renter' else f'02{key}' if user_type == 'rentee' else f'03{key}'

    info_query = (
        "SELECT * FROM cloth_renter WHERE User_ID_id = %s" if user_type == 'renter'
        else "SELECT * FROM cloth_rentee WHERE User_ID_id = %s" if user_type == 'rentee'
        else "SELECT * FROM cloth_delivery_person WHERE User_ID_id = %s"
    )

    info_query_user = "SELECT * FROM cloth_user WHERE User_ID = %s"

    with connection.cursor() as cursor:
        cursor.execute(info_query_user, [user_id])
        user_data = cursor.fetchone()

        if not user_data:
            messages.warning(request, "User not found.")
            return redirect('/login')

        data_info = {
            'user_id': user_data[0],
            'user_name': f'{user_data[1]} {user_data[2]}',
            'phone_number': user_data[4],
        }

        cursor.execute(info_query, [user_id])
        user_specific_data = cursor.fetchone()

        if user_specific_data:
            if user_type == 'renter':
                data_info.update({
                    'user_rating': user_specific_data[2],
                    'user_address': user_specific_data[3],
                    'user_email': user_specific_data[4]
                })
            elif user_type == 'rentee':
                data_info.update({
                    'user_address': user_specific_data[2],
                    'user_email': user_specific_data[3]
                })
            elif user_type == 'dp':
                data_info.update({
                    'user_serial': user_specific_data[1]
                })

            retrieve_pass = "SELECT password FROM cloth_user WHERE User_ID = %s"
            cursor.execute(retrieve_pass, [user_id])
            pass_info = cursor.fetchone()

            if pass_info and pass_info[0] == password:
                return render(request, f'{user_type}-dashboard.html', data_info)
            else:
                messages.warning(request, "Wrong password.")
                return redirect('login')
        else:
            messages.warning(request, "User specific data not found.")
            return redirect('login')



def index(request):
    return render(request, 'index.html')


def product(request):
    if request.method == 'POST':
        try:

            serial_no = request.POST['serial_no']
            clothing_type = request.POST['type']
            condition = request.POST['condition']
            size = request.POST['size']
            category = request.POST['category']
            rent_status = request.POST['rent_status']
            gender = request.POST['gender']
            price = request.POST['price']
            if 'cloth_image' in request.FILES:
                image = request.FILES['cloth_image']
                image_path = default_storage.save(f"media/{image.name}", image)
            else:
                image_path = None

            # Use Django ORM to create a new ClothingItem
            ClothingItem.objects.create(
                Serial_no=serial_no,
                Type=clothing_type,
                Condition=condition,
                Size=size,
                Category=category,
                Rent_status=rent_status,
                Gender=gender,
                Image=image_path,
                Price=price
            )

            messages.success(request, 'Product added successfully.')
            return HttpResponse("hello world")

        except IntegrityError:
            messages.warning(request, 'Product with the same serial number already exists.')
        except Exception as e:
            messages.error(request, f'Error adding product: {e}')

    return render(request, 'product.html')

def login(request):
    return render(request, 'login.html')
def renter_dashboard(request):
    return render(request, 'renter-dashboard.html')
def rentee_dashboard(request):
    return render(request, 'rentee-dashboard.html')
def dp_dashboard(request):
    return render(request, 'dp-dashboard.html')

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
