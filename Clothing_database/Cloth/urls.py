from django.urls import path
from . import views
from .views import dashboard
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [

    path('', views.home, name='homepage'),
    path('dashboard/<str:user_id>', views.dashboard, name='dashboard'),
    path('register_renter', views.register_renter, name='register_renter'),
    path('register_rentee', views.register_rentee, name='register_rentee'),
    path('register_dp', views.register_delivery_person, name='register_delivery_person'),
    path('login', views.login_view, name='login_view'),
    path('edit_profile/<str:user_id>', views.edit_profile, name='edit_profile'),
    path('product', views.product, name='product'),
    path('renter-dashboard',views.renter_dashboard,name='renter_dashboard'),
    path('rentee-dashboard',views.rentee_dashboard,name='rentee_dashboard'),
    path('dp-dashboard',views.dp_dashboard,name='dp_dashboard'),
    path('view_cloth/<str:serial_no>', views.view_cloth, name='view_cloth'),
    path('rentee_home/<str:user_id>/', views.rentee_home, name='rentee_home'),
    path ('cart/<str:user_id>/', views.cart, name = 'cart'),
    # path('checkout/', views.checkout, name='checkout'),
    # path('choose-payment-method/', views.payment_method, name='choose_payment_method'),
    # path('order-placed/',views.order_placed, name= 'order_placed')
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
