from django.contrib import admin
from .models import Product

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin ):
    
    list_display = ( 'product_name', 'price', 'stock', 'category', 'updated_at', 'is_available')
    prepopulated_fields= { 'slug':('product_name',)}