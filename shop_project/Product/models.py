from django.db import models
import uuid
# Create your models here.

class Product():
	product_id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	title=models.CharField(max_length=30)
	descrip=models.TextField(blank=True)
	image=models.ImageField()
	slug=models.SlugField(max_length=30)
	
	''' Every Cart has a relation to a Product  '''

	''' Every Product must reference the Company that published it '''
	#publisher = models.ForeignKey(CustomUser, related_name='products', on_delete=models.CASCADE)

	def __str__(self):
		return self.title