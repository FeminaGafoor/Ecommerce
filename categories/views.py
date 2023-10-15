from django.shortcuts import render,redirect
from categories.models import Category
from django.contrib import messages

# Create your views here.


def category_manage(request):
    category = Category.objects.all()
    context = {
        'category':category
    }
    return render(request,'admini/category_manage.html',context)

def add_categories(request):
    if request.user.is_superuser:
        if request.method == 'POST' :
            category_name = request.POST.get('name')
            category_image = request.FILES.get('image')
            category_description = request.POST.get('description')
            
            # validating whether the field is empty
            
            if category_name.strip() == '':
                messages.error(request, 'field is empty!')
                return redirect('add_categories')
            if Category.objects.filter(name=category_name).exists():
                messages.error(request, 'the category is already taken')
                return redirect('add_categories')
            if not category_image:
                messages.error(request, 'image is not uploaded!')
                return redirect('add_categories')
            if category_description.strip() == '':
                messages.error(request, 'description is not given!')
                return redirect('add_categories')
            
            else:
                new_category = Category(name=category_name,image=category_image,description=category_description)
                
                new_category.save()
                messages.success(request, 'Categories are added successfully')
                return redirect('category_manage')