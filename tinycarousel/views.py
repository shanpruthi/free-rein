from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from tinycarousel.models import Products

# Create your views here.

def index(request):
	template = loader.get_template('tinycarousel/index.html')
	return HttpResponse(template.render(request))

def bout(request):
	template = loader.get_template('tinycarousel/bout.html')
	return HttpResponse(template.render(request))

def shit(request):
	product_list = Products.objects.order_by('-title')
	template = loader.get_template('tinycarousel/shit.html')
	context = {
		'product_list': product_list,
	}
	return HttpResponse(template.render(context, request))