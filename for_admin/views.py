from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def ad_login(request):
    if not request.user.is_superuser:
        return render(request,'admini/index.html')
        
    if request.method == 'POST':    
        username = request.POST['username'] 
        password = request.POST['password'] 
        
        try:
            user_obj = User.objects.get(username = username)

            if  user_obj.is_superuser:
                login(request , user_obj)
                return redirect('for_admin:admin_panel')
            else:
                print('the else is case is working')
                messages.info(request, 'Invalid Username')
                return render(request,'admini/ad_login.html')
            
            
        except ObjectDoesNotExist:
            print('User not found')
            messages.info(request, 'Invalid Username')
            return render(request, 'admini/ad_login.html')
        
    return render(request,'admini/ad_login.html')

    


def admin_panel(request):
    
    if not request.user.is_superuser:
        return render(request,'admini/ad_login.html')
    
    return render(request,'admini/index.html')



def ad_logout(request):
    return render(request,'admini/ad_login.html')
    


def user_manage(request):
    user = User.objects.all()
    context = {
        'users':user
    }
    return render(request,'admini/user_manage.html',context )

def user_block(requset,user_id):
    
    #user is block
    user=User.objects.get(id = user_id)
    if user.is_active:
        user.is_active = False
        user.save()
    else:
        user.is_active = True
        user.save()
    return redirect('for_admin:user_manage')

    


