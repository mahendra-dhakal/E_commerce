from django.db import models

# Create your models here.


class Product(models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    price = models.IntegerField()
    image = models.FileField(upload_to='photos/products')
    stock = models.IntegerField()
    