from django.db import models




class User(models.Model):
    # ROLE_CHOICES = [
    #     ('01', 'Rentee'),
    #     ('02', 'Renter'),
    #     ('03', 'Delivery Person'),
    # ]

    User_ID = models.CharField(max_length=10, primary_key=True)
    First_name = models.CharField(max_length=50)
    Last_name = models.CharField(max_length=50)
    Phone_number = models.CharField(max_length=15)


class Renter(models.Model):
    User_ID = models.ForeignKey(User, on_delete = models.CASCADE, to_field = 'User_ID')
    SSN= models.IntegerField(primary_key=True)
    Rating = models.DecimalField(max_digits=3, decimal_places=2, null=True)
    Address = models.CharField(max_length=80)
    Email = models.CharField(max_length=30)

class Rentee(models.Model):
    User_ID = models.ForeignKey(User, on_delete = models.CASCADE, to_field = 'User_ID')
    NID= models.IntegerField(primary_key=True)
    Shipping_address = models.CharField(max_length=80)
    Email = models.CharField(max_length=30)

class Delivery_person(models.Model):
    User_ID = models.ForeignKey(User, on_delete = models.CASCADE, to_field = 'User_ID')
    Serial_ID= models.IntegerField(primary_key=True)

class Review(models.Model):
    Serial_no = models.ForeignKey('ClothingItem', on_delete=models.CASCADE, to_field='Serial_no')
    Reviews = models.CharField(max_length=50)

class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    Serial_no = models.ForeignKey('ClothingItem', on_delete=models.CASCADE, to_field='Serial_no')
    Name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.Name

class Image(models.Model):
    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'
    
    Serial_no = models.ForeignKey('ClothingItem', on_delete=models.CASCADE, to_field='Serial_no')
    image = models.CharField(max_length=100, null=True, blank=False)
    

    def __str__(self):
        return self.description

class ClothingItem(models.Model):
    Serial_no = models.CharField(max_length=12, primary_key=True)
    Type = models.CharField(max_length=10)
    Condition = models.CharField(max_length=10)
    Size = models.IntegerField()
    Rent_status = models.CharField(max_length=10)
    Gender = models.CharField(max_length=10)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Rating = models.DecimalField(max_digits=3, decimal_places=2, null=True)
    Reviews = models.ManyToManyField(Review, related_name='ClothingItem')
    Category = models.ManyToManyField(Category, related_name='ClothingItem')
    Image = models.ManyToManyField(Image, related_name='ClothingItem')


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