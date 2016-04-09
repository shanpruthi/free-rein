from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from tinycarousel.models import Products

# Create your views here.

def index(request):
	template = loader.get_template('tinycarousel/index.html')
	return HttpResponse(template.render(request))

def about(request):
	template = loader.get_template('tinycarousel/about.html')
	return HttpResponse(template.render(request))

def products(request):
	product_list = Products.objects.order_by('-title')
	template = loader.get_template('tinycarousel/products.html')
	context = {
		'product_list': product_list,
	}
	return HttpResponse(template.render(context, request))