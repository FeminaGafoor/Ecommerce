from django.shortcuts import render

# Create your views here.
def shipping_address(request):
    return render(request,'user/shipping_address.html')

def payments(request):
    return render(request,'user/payments.html')


def summary(request):
    return render(request,'user/summary.html')


def finish(request):
    return render(request,'user/finish.html')