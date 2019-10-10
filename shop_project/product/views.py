from django.shortcuts import render , redirect, get_object_or_404
from django.http import HttpResponse
from .models import Product
from .forms import ProductForm
from Users.decorators import *
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request,*args,**kwargs):
	products=Product.objects.order_by('-title')
	
	return render(request,'product_home.html',{'products' : products }) 


@login_required
@company_required
def new_product(request,*args,**kwargs):
	if request.method == "POST":
		form = ProductForm(request.POST, request.FILES)

		if form.is_valid():
			post = form.save(commit=False)
			if request.user.is_authenticated:
				post.publisher=request.user
			post.save()
			#return redirect('post_detail', pk=post.pk)
			return redirect('product_detail',slug=post.slug)
	else:
		form = ProductForm()
	return render(request, 'product_new.html', {'form': form})

def success(request):
	return HttpResponse('Success')

def product_detail(request,slug):
	
	product=Product.objects.get(slug=slug)
	return render(request,'product_detail.html',{'product':product })

@login_required
@company_required
def product_edit(request,slug,*args,**kwargs):
	post = get_object_or_404(Product, slug=slug)
	if request.method == "POST":
		form = ProductForm(request.POST, request.FILES , instance=post)

		if form.is_valid():
			post = form.save(commit=False)
			if request.user.is_authenticated:
				post.publisher=request.user
			post.save()
			#return redirect('post_detail', pk=post.pk)
			return redirect('product_detail',slug=post.slug)
	else:
		form = ProductForm(instance=post)
	return render(request, 'product_edit.html', {'form': form , 'Product':post})