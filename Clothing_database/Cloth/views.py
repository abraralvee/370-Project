from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.contrib import messages
from django.db import connection
from django.core.files.storage import default_storage
from .models import ClothingItem, Review
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseServerError
from django.http import JsonResponse
from .models import ClothingItem, Cart, User

# Maisha Tasnim- 21201117
# Maisha Tasnim- 21201117
# Maisha Tasnim- 21201117
# Maisha Tasnim- 21201117

def home(request):
    return render(request, 'homepage.html')

def renter_dashboard(request):
    return render(request, 'renter-dashboard.html')

def rentee_dashboard(request):
    return render(request, 'rentee-dashboard.html')

def dp_dashboard(request):
    return render(request, 'dp-dashboard.html')

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
    
        find_user = "SELECT user_id FROM cloth_user WHERE user_id = %s"
        insert_user = 'insert into cloth_user (user_id, first_name, last_name, password, phone_number) values (%s, %s,%s, %s, %s)'
        insert_rentee = 'insert into cloth_rentee (User_ID_id, NID,  Shipping_address, email) values ( %s, %s, %s, %s) '

        with connection.cursor() as cursor:
                cursor.execute(find_user, (user_id,))
                existing_user = cursor.fetchone()
                if existing_user:
                    messages.warning(request, 'You already have an account')
                    return redirect('/login')
                else:
                    cursor.execute(insert_user, (user_id, first_name, last_name, password, phone))
                    cursor.execute(insert_rentee, (user_id, NID, address, email))
                    messages.success(request, 'Signup Successful')
                    return redirect('dashboard', user_id=user_id)
                
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
                    return redirect('dashboard', user_id=user_id)
                
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
    
        find_user = "SELECT user_id FROM cloth_user WHERE user_id = %s"
        insert_user = 'insert into cloth_user (user_id, first_name, last_name, password, phone_number) values (%s, %s,%s, %s, %s)'
        insert_dp = 'insert into cloth_delivery_person (User_ID_id, SSN) values ( %s, %s) '

        with connection.cursor() as cursor:
                cursor.execute(find_user, (user_id,))
                existing_user = cursor.fetchone()
                if existing_user:
                    messages.warning(request, 'You already have an account')
                    return redirect('/login')
                else:
                    cursor.execute(insert_user, (user_id, first_name, last_name, password, phone))
                    cursor.execute(insert_dp, (user_id, SSN))
                    messages.success(request, 'Signup Successful')
                    return redirect('dashboard', user_id=user_id)
                
    return render(request, 'register_dp.html')


def dashboard(request, user_id):
    if user_id[:2] =='01':
        user_type= 'renter'
        info_query = "SELECT * FROM cloth_renter WHERE User_ID_id = %s"
        rented_clothes_query = "SELECT * FROM cloth_Clothingitem WHERE renter_id_id = %s"
    elif user_id[:2] =='02':
        user_type= 'rentee'
        info_query = "SELECT * FROM cloth_rentee WHERE User_ID_id = %s"
    else:
        user_type= 'dp'
        info_query = "SELECT * FROM cloth_delivery_person WHERE User_ID_id = %s"

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
                    'user_rating': user_specific_data[1],
                    'user_address': user_specific_data[2],
                    'user_email': user_specific_data[3]
                })
                with connection.cursor() as cursor:
                    cursor.execute(rented_clothes_query, [user_id])
                    rented_clothes_data = cursor.fetchall()

                    rented_clothes_list = []
                    for rented_clothes in rented_clothes_data:
                        rented_clothes_info = {
                        'type': rented_clothes[1],
                        'serial_no': rented_clothes[0],
                        'rental_status': rented_clothes[5],
                        'price': rented_clothes[8],
                        }
                        rented_clothes_list.append(rented_clothes_info)
                    data_info['rented_clothes'] = rented_clothes_list
            elif user_type == 'rentee':
                data_info.update({
                    'user_address': user_specific_data[1],
                    'user_email': user_specific_data[2]
                })
            elif user_type == 'dp':
                data_info.update({
                    'user_serial': user_specific_data[0]
                })

    if user_type == 'renter':
        template_name = 'renter-dashboard.html'
        
    elif user_type == 'rentee':
        template_name = 'rentee-dashboard.html'
    elif user_type == 'dp':
        template_name = 'dp-dashboard.html'

    return render(request, template_name, data_info)


def login_view(request):
    if request.method == "POST":
        key = request.POST.get('key')
        user_type = request.POST.get('user_type')
        password = request.POST.get('password')

        if user_type == 'renter':
            user_id = '01' + key
        elif user_type == 'rentee':
            user_id = '02' + key
        elif user_type == 'dp':
            user_id = '03' + key

        info_query_user = "SELECT * FROM cloth_user WHERE User_ID = %s"

        with connection.cursor() as cursor:
            cursor.execute(info_query_user, [user_id])
            user_data = cursor.fetchone()

            if not user_data:
                messages.warning(request, "User not found.")
                return redirect('/login')
            else:
                retrieve_pass = "SELECT password FROM cloth_user WHERE User_ID = %s"
                cursor.execute(retrieve_pass, [user_id])
                pass_info = cursor.fetchone()
                if pass_info and pass_info[0] == password:
                    return redirect('dashboard', user_id=user_id)
                else:
                    messages.warning(request, "Wrong password.")
            
    return render(request, 'login.html')



def edit_profile(request, user_id):
    if request.method == 'POST':
        new_first_name = request.POST.get('new_first_name')
        new_last_name = request.POST.get('new_last_name')
        new_phone_number = request.POST.get('new_phone_number')

        
        update_query = "UPDATE cloth_user SET First_name = %s, Last_name = %s, Phone_number = %s WHERE User_ID = %s"
        with connection.cursor() as cursor:
            cursor.execute(update_query, [new_first_name, new_last_name, new_phone_number, user_id])

        messages.success(request, "Profile updated successfully.")
        return redirect('dashboard', user_id=user_id)


    info_query_user = "SELECT * FROM cloth_user WHERE user_id = %s"
    with connection.cursor() as cursor:
        cursor.execute(info_query_user, [user_id])
        user_data = cursor.fetchone()

        if not user_data:
            messages.warning(request, "User not found.")
            return redirect('dashboard', user_id=user_id)

        data_info = {
            'user_id': user_data[0],
            'user_first_name': user_data[1],
            'user_last_name': user_data[2],
            'user_phone_number': user_data[4],
        }

    return render(request, 'edit_profile.html', data_info)

from .models import User

def delete_rented_item(request, serial_no):
    rented_item = get_object_or_404(ClothingItem, Serial_no=serial_no)
    user_id= rented_item.renter_id_id

    if rented_item.Rent_status == 'available':
        rented_item.delete()

    return redirect('dashboard', user_id)

from .models import Renter, Rentee, Delivery_person, User

def delete_profile(request, user_id):
    user_type = user_id[:2]

    if user_type == '01':
        model_class = Renter
    elif user_type == '02':
        model_class = Rentee
    elif user_type == '03':
        model_class = Delivery_person

    try:
        if user_type == '01':
            rented_items = ClothingItem.objects.filter(renter_id_id=user_id, Rent_status='rented')
            if rented_items.exists():
                messages.error(request, "You cannot delete your account because you have rented items.")
                return redirect('dashboard', user_id)

        user_instance = get_object_or_404(model_class, User_ID_id=user_id)
        user_instance.delete()

    except model_class.DoesNotExist:
        return redirect('/')  

    try:
        user = get_object_or_404(User, User_ID=user_id)
        user.delete()
        messages.success(request, "Account deleted successfully.")
        return redirect('/')
    except User.DoesNotExist:
        return redirect('/')






#Abrar Jahin Alvee- 21201226
#Abrar Jahin Alvee- 21201226
#Abrar Jahin Alvee- 21201226
#Abrar Jahin Alvee- 21201226


def product(request, user_id):
    renter_id= user_id
    context = {'user_id': user_id}

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
            
            find_product_query = "SELECT * FROM cloth_clothingitem WHERE Serial_no = %s"
            with connection.cursor() as cursor:
                cursor.execute(find_product_query, [serial_no])
                existing_product = cursor.fetchone()

            if existing_product:
                messages.warning(request, 'Product with the same serial number already exists.')
                return render(request, 'product.html', context)

            if 'cloth_image' in request.FILES:
                image = request.FILES['cloth_image']
                image_path = default_storage.save(f"{image}", image)
            else:
                image_path = None

            insert_product_query = """
            INSERT INTO cloth_ClothingItem (Serial_no, Type, `Condition`, Size, Category, Rent_status, Gender, Image, Price, renter_id_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            with connection.cursor() as cursor:
                cursor.execute(insert_product_query, [serial_no, clothing_type, condition, size, category, rent_status, gender, image_path, price, renter_id])

            messages.success(request, 'Product added successfully.')
            return redirect('product_detail', serial_no=serial_no)

        except Exception as e:
            messages.error(request, f'Error adding product: {e}')
            return HttpResponseServerError(f'Internal Server Error: {e}')

    return render(request, 'product.html', context)

def rentee(request):
    search_query = request.GET.get('search_query', '')
    category_query = request.GET.get('Category')

    if search_query:
        item_data = ClothingItem.objects.filter(Type__icontains=search_query)
    elif category_query:
        item_data = ClothingItem.objects.filter(Category__icontains=category_query)
    else:
        item_data = ClothingItem.objects.all()

    item_data_with_images = []
    for item in item_data:
        images = item.Image
        item_data_with_images.append({'item': item, 'images': images})

    data = {'item_data_with_images': item_data_with_images}

    return render(request, 'rentee.html', data)

def product_detail_view(request, serial_no):
    product = ClothingItem.objects.get(Serial_no=serial_no)
    reviews = product.Reviews.all()  
    images = product.Image
    context = {'product': product, 'images': images, 'reviews': reviews}
    return render(request, 'product_detail.html', context)

def submit_comment(request, serial_no):
    if request.method == 'POST':
        customer_name = request.POST.get('customer_name')
        new_comment = request.POST.get('new_comment')
        rating = request.POST.get('rating')

        clothing_item = ClothingItem.objects.get(Serial_no=serial_no)
        review = Review.objects.create(Serial_no_id=serial_no, Reviews=new_comment)

        return redirect('review_detail', review_id=review.id)
    if 'redirect_to_review' in request.GET:
        return redirect('review_detail', review_id=review.id, submitted=True)
    return redirect('product_detail', serial_no=serial_no)

def submit_rating(request, serial_no):
    if request.method == 'POST':
        new_rating = int(request.POST.get('new_rating', 0))
        if 1 <= new_rating <= 5:
            product = get_object_or_404(ClothingItem, Serial_no=serial_no)
            product.Rating = new_rating
            product.save() 
    return redirect('product_detail', serial_no=serial_no)

def review_detail_view(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    return render(request, 'review_detail.html', {'review': review})


def rentee_home(request, user_id):
    try:
        user_profile = User.objects.get(User_ID=user_id)
    except User.DoesNotExist:
       return HttpResponse("/cart/")

    products = ClothingItem.objects.all()
    for product in products:
        product.star_range = range(int(product.Rating or 0))

    context = {
        'user_info': {
            'user_id': user_profile.User_ID,
            'user_first_name': user_profile.First_name,
            'user_last_name': user_profile.Last_name,
            'user_phone_number': user_profile.Phone_number,
        },
        'products': products,
    }
    return render(request, 'rentee_home.html', context)









# Fairuz Binte Khaled- 22101664
# Fairuz Binte Khaled- 22101664
# Fairuz Binte Khaled- 22101664
# Fairuz Binte Khaled- 22101664


def checkout(request):
    return render(request, 'credit_card.html')

def payment_method(request):
    return render(request, 'payment_method.html')

def order_placed(request):
    return render(request, 'order_placed.html')

def cart(request, user_id):
    product_query = 'SELECT * FROM cloth_cart WHERE user_id = %s'
    
    with connection.cursor() as cursor:
        cursor.execute(product_query, [user_id])
        items = cursor.fetchall() 
    products = []
    for item in items:
        product = {
            'column_name_1': item[0],
            'column_name_2': item[1],
            
        }
        products.append(product)

    return render(request, 'cart.html', {'products': products})


def add_to_cart(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        serial_no = request.POST.get('serial_no')
        
        find_user = "SELECT Cart_number FROM cloth_cart"
        insert_cloth = 'INSERT INTO cloth_cart (Cart_number,User_ID, Product_id) VALUES (%s, %s,%s)'

        with connection.cursor() as cursor:
                obj = User.objects.get(pk=user_id)
                cart_no = cursor.execute(find_user) + 20
                print(cart_no) 
                cursor.execute(insert_cloth, (cart_no,obj,serial_no))
                
    

        return JsonResponse({'success': True, 'quantity': 'DONE'})
    return JsonResponse({'success': False})

    
from .forms import BkashTransactionForm

def bkash_transaction(request):
    if request.method == 'POST':
        form = BkashTransactionForm(request.POST)
        if form.is_valid():
            return  redirect(order_placed)  
    else:
        form = BkashTransactionForm()

    return render(request, 'bkash-transaction.html', {'form': form})
def nagad_transaction(request):
    if request.method == 'POST':
        form = BkashTransactionForm(request.POST)
        if form.is_valid():
            return  HttpResponse('Transaction Succesful')  
    else:
        form = BkashTransactionForm()

    return render(request, 'nagad_transaction.html', {'form': form})