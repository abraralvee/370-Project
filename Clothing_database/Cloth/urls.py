from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('Renter-login/', views.renter_login, name='Renter Registration'),
    path('Rentee-login/', views.rentee_login, name='Rentee Registration'),
    path('login/', views.login_view, name='login')
    path('clothing-items/', clothing_items, name='clothing_items'),
    path('renter-portal/', renter_portal, name='renter_portal')
]
