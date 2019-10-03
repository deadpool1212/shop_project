from django.db import models
import uuid
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.datetime_safe import datetime
# Create your models here.

class Product(models.Model):
	product_id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	title=models.CharField(max_length=30,unique=True)
	descrip=models.TextField(blank=True)
	image=models.ImageField(upload_to='images/')
	cost = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
	slug=models.SlugField(max_length=30,null=True)
	published_date=models.DateTimeField(auto_now_add=True)
	last_edited=models.DateTimeField(auto_now=True)
	''' Every Cart has a relation to a Product  '''

	''' Every Product must reference the Company that published it '''
	publisher = models.ForeignKey(User, related_name='products', on_delete=models.CASCADE)

	def __str__(self):
		return self.title


class Cart(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete='CASCADE')
    count = models.PositiveIntegerField(default=0)
    total = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "User: {} has {} items in their cart. Their total is ${}".format(self.user, self.count, self.total)


class Entry(models.Model):
    product = models.ForeignKey('Product', null=True, on_delete='CASCADE')
    cart = models.ForeignKey('Cart', null=True, on_delete='CASCADE')
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return "This entry contains {} {}(s).".format(self.quantity, self.product.title)


@receiver(post_save, sender=Entry)
def update_cart(sender, instance, **kwargs):
    line_cost = instance.quantity * instance.product.cost
    instance.cart.total += line_cost
    instance.cart.count += instance.quantity
    instance.cart.updated = datetime.now()