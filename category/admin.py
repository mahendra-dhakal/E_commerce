from django.contrib import admin
from .models import Category

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('category_name',)}   #by default write down slug field in django admin panel . we dont need to manually write down .
    list_display=('category_name','description','slug')
    search_fields=('category_name','description','slug')