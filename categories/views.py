from django.shortcuts import render

# Create your views here.
def categories(request):
    return render(request,'user/categories.html')

def mens(request):
    return render(request,'user/mens.html')


def kids(request):
    return render(request,'user/kids.html')
    