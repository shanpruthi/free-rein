from django.contrib import admin
from .models import Products

# Register your models here.

class ProductsAdmin(admin.ModelAdmin):
	list_display = ('title', 'description', 'price')
	list_filter = ('title', 'price')

admin.site.register(Products, ProductsAdmin)