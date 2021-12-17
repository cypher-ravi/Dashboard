
from django.urls import path,include
from .views import index

from .views import login_view

from .views import *
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static


app_name = 'dashboard'

urlpatterns =[
   path('', index, name = 'AdminHome'),
   path('search', search),
   path('login/', login_view, name="login"),
   # path('register/', register_user, name="register"),
   path("logout/", logout_view, name="logout"),
  

  

   path('new_vendor/',NewVendorView.as_view(),name='NewVendor'), 
   path('vendor_requests/',VendorRequestView.as_view(),name='VendorRequest'), 
   # path('all_vendors/',AllVendorsView.as_view(),name='AllVendors'), 
   # path('vendor/<int:pk>/', DetailVendorView.as_view(), name='vendor_detail'),





   #for contact
   path('contact/',ContactUsView.as_view(),name='contact'), 
   

  # for template testing
   # path('test_view/',TestView.as_view(),name='NewTest'),

  




]

if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
