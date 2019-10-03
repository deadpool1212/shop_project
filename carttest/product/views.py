from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Product
from .forms import ProductForm
# Create your views here.

def home(request,*args,**kwargs):
	products=Product.objects.order_by('-title')
	
	return render(request,'home.html',{'products' : products }) 

def new_product(request,*args,**kwargs):
	if request.method == "POST":
		form = ProductForm(request.POST, request.FILES)

		if form.is_valid():
			post = form.save(commit=False)
			if request.user.is_authenticated:
				post.publisher=request.user
			post.save()
			#return redirect('post_detail', pk=post.pk)
			return redirect('success')
	else:
		form = ProductForm()
	return render(request, 'product_edit.html', {'form': form})

def success(request):
	return HttpResponse('Success')