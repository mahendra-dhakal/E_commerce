from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description= models.TextField(blank=True)
    cat_image = models.ImageField(upload_to='photos/categories/', blank=True, null=True)
    
    def __str__(self):
        return self.category_name
    
    class Meta:
        verbose_name='category'
        verbose_name_plural='categories'