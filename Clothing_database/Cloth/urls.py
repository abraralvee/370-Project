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
    path('product/<str:user_id>', views.product, name='product'),
    path('renter-dashboard',views.renter_dashboard,name='renter_dashboard'),
    path('rentee-dashboard',views.rentee_dashboard,name='rentee_dashboard'),
    path('dp-dashboard',views.dp_dashboard,name='dp_dashboard'),
    # path('view_cloth/<str:serial_no>', views.view_cloth, name='view_cloth'),
    path('delete_rented_item/<str:serial_no>', views.delete_rented_item, name='delete_rented_item'),
    path ('cart/<str:user_id>/', views.cart, name = 'cart'),
    path('delete_profile/<str:user_id>', views.delete_profile, name='delete_profile'),
    # path('checkout/', views.checkout, name='checkout'),
    # path('choose-payment-method/', views.payment_method, name='choose_payment_method'),
    # path('order-placed/',views.order_placed, name= 'order_placed')
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('rentee', views.rentee, name='rentee'),
    # path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('submit_rating/<str:serial_no>/', views.submit_rating, name='submit_rating'),
    path('product_detail/<str:serial_no>/', views.product_detail_view, name='product_detail'),
    # path('search_results/', views.search_results, name='search_results'),
    path('review_detail/<int:review_id>/', views.review_detail_view, name='review_detail'),
    path('submit_comment/<str:serial_no>/', views.submit_comment, name='submit_comment'),




    path('rentee_home/<str:user_id>/', views.rentee_home, name='rentee_home'),
    path('checkout/', views.checkout, name='checkout'),
    path('payment-method/', views.payment_method, name='payment_method'),
    path('order-placed/',views.order_placed, name= 'order_placed'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('cart/<str:user_id>/', views.cart, name='cart'),
    # path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('bkash-transaction/', views.bkash_transaction, name='bkash_transaction'),
    path('nagad-transaction/', views.nagad_transaction, name='nagad_transaction'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
