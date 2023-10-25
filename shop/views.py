from django.shortcuts import render
from django.shortcuts import render, get_object_or_404

from items.models import Category, Products,ProductImage


# Create your views here.


def shop(request):
    product = Products.objects.all()
    image = ProductImage.objects.all()
    context = {
        'product': product,
        'image': image,
    }
    return render(request, 'user/shop.html', context)



def product(request, product_id):
    print(f"Product view called with product_id={product_id}")
    
    image = ProductImage.objects.all()
    # Add any additional context you want to pass to the product.html template
    context = {
        'product': product,
        'image': image,
    }
  
    return render(request, 'user/product.html', context)


def category(request):
    category = Category.objects.all()
 
    context = {
        'category':category
    }
    return render(request,'user/categories.html',context)


def womens(request):
    return render(request,'user/womens.html')

def mens(request):
    return render(request,'user/mens.html')

def kids(request):
    return render(request,'user/kids.html')