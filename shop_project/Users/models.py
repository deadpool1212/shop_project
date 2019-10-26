from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from .managers import CustomUserManager
import uuid
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.datetime_safe import datetime
from django.template.defaultfilters import slugify
# Create your models here.

class Product(models.Model):
    product_id=models.UUIDField(primary_key=True, default=uuid.uuid4)
    title=models.CharField(max_length=30,unique=True)
    descrip=models.TextField(blank=True)
    image=models.ImageField(upload_to='images/')
    cost = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    slug=models.SlugField(max_length=30,null=True,unique=True)
    published_date=models.DateTimeField(auto_now_add=True)
    last_edited=models.DateTimeField(auto_now=True)
    readonly_fields=('product_id',)
    ''' Every Cart has a relation to a Product  '''

    ''' Every Product must reference the Company that published it '''
    publisher = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='products', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Product, self).save(*args, **kwargs)


class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)
    total = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    products = models.ManyToManyField(Product , blank=True)


    def __str__(self):
        return "User: {} has items in their cart. Their total is ${}".format(self.user, self.total)
    def save(self, *args, **kwargs):
        self.total=0
        for product in self.products.all():
            self.total+=product.cost
        super(Cart, self).save(*args, **kwargs)


    def get_all_products(self):
        product=[]
        for prod in self.products:
            product.append(prod)
        return product



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