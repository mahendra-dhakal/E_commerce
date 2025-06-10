from django.contrib import admin
from .models import Category

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=('category_name','description','cat_image','slug')
    search_fields=('category_name','description','slug')