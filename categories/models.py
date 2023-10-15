from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField( max_length=50, blank=True, default=True, null=True)
    image = models.ImageField( upload_to='images',height_field=None, width_field=None, max_length=None,default=True)
    category_description = models.CharField( max_length=50, blank=True, default=True, null=True)
    create = models.DateField(auto_now_add=True)
    update = models.DateField(auto_now=True)
    
    class Meta:
        verbose_name   ='Category'
        verbose_name_plural='name'