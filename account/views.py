from django.shortcuts import render,redirect
from django.contrib.auth import authenticate ,login,logout
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def user_login(request):
    # if request.user.is_authenticated:
        
    #     return redirect('home:home')
   
    if request.method == "POST" :
        
        username=request.POST['username']
        password=request.POST['password']
        email=request.POST['email']
        
        user = authenticate(username=username,email=email,password=password)
    
        if user is not None:
            login(request,user)
            return redirect('home:home')
        
        else:
            messages.error(request,'Invalid Credentials')
            return redirect('account:user_login')

    return render(request,'user/login.html')


def register(request):
    if request.method == 'POST':
 
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        repassword=request.POST['re_password']
        if password != repassword:
            messages.error(request,'Invalid Password')
        elif username.strip()=='' or email.strip()=='' or password.strip()=='':
            messages.error(request,'Field Cannot Be Empty')
        else:
            user=User.objects.create_user(username=username,email=email,password=password)
            user.save()
            return redirect('account:user_login')
   
    return render(request,'user/register.html')


