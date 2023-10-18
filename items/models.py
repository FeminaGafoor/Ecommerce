from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField( max_length=50, blank=True, default=True, null=True)
    image = models.ImageField( upload_to='images/',height_field=None, width_field=None, max_length=None,default=True)
    category_description = models.CharField( max_length=50, blank=True, default=True, null=True)
    create = models.DateField(auto_now_add=True)
    update = models.DateField(auto_now=True)
    
    
    def __str__(self):
        return self.name
    
    
class Brand(models.Model):
    brand_name = models.CharField(max_length=50,blank=True,null=True)
    brand_image = models.ImageField( upload_to='brand_img/', height_field=None, width_field=None, max_length=None)
    
    
    def __str__(self):
        return self.brand_name
    
class Color(models.Model):
    name = models.CharField(max_length= 10)
    
class Size(models.Model):
    name = models.CharField(max_length= 10)   
    
class Products(models.Model):
    name = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    brand = models.ForeignKey(Brand, blank=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    colors = models.ManyToManyField(Color)
    size = models.ManyToManyField(Size)
    stock = models.CharField(max_length=100,blank=True)
    is_deleted = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
class ProductImage(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/',blank=True)
    
    def __str__(self):
        return self.product
    
    
    
       
    
    

