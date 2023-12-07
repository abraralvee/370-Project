from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('', views.home, name='homepage'),
    path('register_renter/', views.register_renter, name='Renter Registration'),
    path('register_rentee/', views.register_rentee, name='Rentee Registration'),
    path('renter_login/', views.renter_login_view, name='renter_login'),
    path('renter-dashboard/',views.renter_dashboard,name='Renter dashboard'),
    path('rentee_home/', views.rentee_home, name= 'rentee_home'),
    path('rentee_login/', views.rentee_login_view, name='rentee_login'),
    path ('cart/', views.cart, name = 'cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('choose-payment-method/', views.payment_method, name='choose_payment_method'),
    path('order-placed/',views.order_placed, name= 'order_placed')
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]