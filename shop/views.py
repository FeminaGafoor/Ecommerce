from django.shortcuts import render

# Create your views here.
def shop(request):
    return render(request,'user/shop.html')

def product(request):
    return render(request,'user/product.html')