from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [

    path('', views.home, name='homepage'),
    path('register_renter', views.register_renter, name='register_renter'),
    path('register_rentee', views.register_rentee, name='register_rentee'),
    path('register_dp', views.register_delivery_person, name='register_delivery_person'),
    path('login', views.login_view, name='login_view'),
    path('product', views.product, name='product'),
    path('renter-dashboard',views.renter_dashboard,name='renter_dashboard'),
    path('rentee-dashboard',views.rentee_dashboard,name='rentee_dashboard'),
    path('dp-dashboard',views.dp_dashboard,name='dp_dashboard')
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
