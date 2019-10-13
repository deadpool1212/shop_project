from django.contrib import admin
from django.urls import path, include, re_path
from .views import *
#from django.conf.urls.static import static
from django.contrib.staticfiles.urls import static
from django.conf import settings
import uuid
urlpatterns = [
    
    path('',home,name='home' ),
    re_path(r'^new/$',new_product , name='new'),
    re_path(r'^success/$', success, name = 'success'), 
    path('detail/<slug:slug>/',product_detail,name='product_detail'),
    path('change/<slug:slug>/',product_edit,name='product_edit'),
    path('cart/',cart_view, name='cart_view'),
]

urlpatterns += [
	path('signupcustomer/', CustomerSignUpView.as_view(), name='signupcustomer'),
	path('signupcompany/', CompanySignUpView.as_view(), name='signupcompany'),
	

]