from django.db import models
from Users.models import CustomUser
# Create your models here.

class Product():
	title=models.CharField()
	descrip=models.TextField()
	image=models.ImageField()
	Publisher=OneToOneField(CustomUser)
	