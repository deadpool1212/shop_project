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
    path('<slug:slug>/detail/',product_detail,name='product_detail')
]

