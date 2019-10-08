from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import *
from django.db import transaction

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email','phone_number','is_company')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email','phone_number' , 'is_company')

class CustomerSignUpForm(UserCreationForm):
    Address=forms.CharField()

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email','phone_number','username')

    @transaction.atomic
    def save(self):
        User = super().save(commit=False)
        User.is_company = False
        User.save()
        customer = Customer.objects.create(User=User)
        customer.Address=self.cleaned_data.get('Address')
        customer.save()
        return User

class CompanySignUpForm(UserCreationForm):
    domain=forms.URLField()

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email','phone_number','username')

    @transaction.atomic
    def save(self):
        User = super().save(commit=False)
        User.is_company = True
        User.save()
        company = Company.objects.create(User=User)
        company.domain=(self.cleaned_data.get('domain'))
        company.save()
        return User