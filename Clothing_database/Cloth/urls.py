from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('', views.home, name='homepage'),
    path('register_renter/', views.register_renter, name='Renter Registration'),
    path('register_rentee/', views.register_rentee, name='Rentee Registration'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]