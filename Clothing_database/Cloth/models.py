# models.py

from django.db import models

class User(models.Model):
    User_ID = models.CharField(max_length=20, primary_key=True, unique=True)
    First_name = models.CharField(max_length=50)
    Last_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    Phone_number = models.CharField(max_length=15)

class Renter(models.Model):
    User_ID = models.ForeignKey(User, on_delete=models.CASCADE)
    SSN = models.CharField(max_length=15, primary_key=True, default='')
    Rating = models.DecimalField(max_digits=3, decimal_places=2, null=True)
    Address = models.CharField(max_length=80)
    Email = models.CharField(max_length=30)

class Rentee(models.Model):
    User_ID = models.ForeignKey(User, on_delete=models.CASCADE)
    NID = models.CharField(max_length=15, primary_key=True, default='')
    Shipping_address = models.CharField(max_length=80)
    Email = models.CharField(max_length=30)

class Delivery_person(models.Model):
    User_ID = models.ForeignKey(User, on_delete=models.CASCADE)
    SSN = models.CharField(max_length=15, primary_key=True)


class Review(models.Model):
    Serial_no = models.ForeignKey('ClothingItem', on_delete=models.CASCADE, to_field='Serial_no')
    Reviews = models.CharField(max_length=50)

class ClothingItem(models.Model):
    Serial_no = models.CharField(max_length=12, primary_key=True)
    Type = models.CharField(max_length=10)
    Condition = models.CharField(max_length=10)
    Size = models.IntegerField()
    Category = models.CharField(max_length=10)
    Rent_status = models.CharField(max_length=10)
    Gender = models.CharField(max_length=10)
    Image = models.CharField(max_length=50, null=True)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Rating = models.IntegerField(default=0)
    Reviews = models.ManyToManyField(Review, related_name='clothing_items')
    renter_id= models.ForeignKey(User, on_delete=models.CASCADE, null=True)

class Cart(models.Model):
    Cart_number = models.IntegerField(primary_key=True)
    Voucher = models.CharField(max_length=10)
    Daily_charge= models.DecimalField(max_digits=10, decimal_places=2)
    Delivery_charge = models.DecimalField(max_digits=10, decimal_places=2)
    Duration = models.DurationField()
    Product_price = models.DecimalField(max_digits=10, decimal_places=2)

class Transaction(models.Model):
    Transaction_iD = models.CharField(max_length=12, primary_key=True)
    Total_payment = models.DecimalField(max_digits=10, decimal_places=2)

class Bkash(models.Model):
    Transaction_iD = models.ForeignKey(Transaction, on_delete = models.CASCADE, to_field = 'Transaction_iD')
    Phone_no = models.CharField(max_length=15)

class Nagad(models.Model):
    Transaction_iD = models.ForeignKey(Transaction, on_delete = models.CASCADE, to_field = 'Transaction_iD')
    Phone_no = models.CharField(max_length=15)

class Visa_card(models.Model):
    Transaction_iD = models.ForeignKey(Transaction, on_delete = models.CASCADE, to_field = 'Transaction_iD')
    First_name = models.CharField(max_length=50)
    Last_name = models.CharField(max_length=50)
    Card_number = models.IntegerField()