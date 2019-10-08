from django.urls import path
from . import views


urlpatterns = [
	path('signupcustomer/', views.CustomerSignUpView.as_view(), name='signupcustomer'),
	path('signupcompany/', views.CompanySignUpView.as_view(), name='signupcompany'),
	

]