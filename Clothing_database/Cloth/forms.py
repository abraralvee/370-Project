from django import forms
from .models import User, Renter, Rentee, Delivery_person

class RenteeRegistrationForm(forms.ModelForm):
    class Meta:
        model = Rentee
        fields = ['User_ID', 'NID', 'Shipping_address', 'Email']

class RenterRegistrationForm(forms.ModelForm):
    class Meta:
        model = Renter
        fields = ['User_ID', 'SSN', 'Rating', 'Address', 'Email']

class DeliveryPersonRegistrationForm(forms.ModelForm):
    class Meta:
        model = Delivery_person
        fields = ['User_ID', 'Serial_ID']