from django import forms

class BkashTransactionForm(forms.Form):
    phone_number = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}))
    transaction_id = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Transaction ID'}))

class NagadTransactionForm(forms.Form):
    phone_number = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}))
    transaction_id = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Transaction ID'}))               