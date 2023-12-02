from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


def home(request):
    return render(request, 'homepage.html')
def renter_login(request):
    return render(request, 'Renter-login.html')
def rentee_login(request):
    return render(request, 'Rentee-login.html')
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('index')  # Change 'index' to the name of your home page URL
        else:
            # Return an 'invalid login' error message.
            return render(request, 'login.html', {'error': 'Invalid login credentials'})

    return render(request, 'login.html')