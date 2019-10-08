from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    phone_number = models.IntegerField()
    is_company = models.BooleanField()
    username=models.CharField(max_length=30,unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number','is_company', 'username']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class Customer(models.Model):
    User=models.OneToOneField(CustomUser,on_delete=models.CASCADE, primary_key=True)
    Address=models.CharField(max_length=255)
    def __str__(self):
        return self.User.email

class Company(models.Model):
    User=models.OneToOneField(CustomUser,on_delete=models.CASCADE, primary_key=True)
    domain=models.URLField()
    def __str__(self):
        return self.User.email