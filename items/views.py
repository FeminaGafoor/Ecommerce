from django.shortcuts import render,redirect, get_object_or_404
from items.models import Category
from .models import Brand, Color, Products ,Size

from django.contrib import messages

# Create your views here.


#CATAGORY_MANAGE---------------------------------------------------------------------------

def category_manage(request):
    category = Category.objects.all()
    print(category)
    context = {
        'category':category
    }
    return render(request,'admini/category_manage.html',context)

def add_categories(request):
    if request.user.is_superuser:
        if request.method == 'POST' :
            category_name = request.POST.get('name')
            category_image = request.FILES.get('image')
            description = request.POST.get('description')
            print(description)
            # validating whether the field is empty
            
            if category_name.strip() == '':
                messages.error(request, 'field is empty!')
                return redirect('items:add_categories')
            elif Category.objects.filter(name=category_name).exists():
                messages.error(request, 'the category is already taken')
                return redirect('items:add_categories')
            elif not category_image:
                messages.error(request, 'image is not uploaded!')
                return redirect('items:add_categories')
            elif description.strip() == '':
                messages.error(request, 'description is not given!')
                return redirect('items:add_categories')
            
            else:
                new_category = Category.objects.create(name=category_name,image=category_image,category_description=description)
                
                new_category.save()
                messages.success(request, 'Categories are added successfully')
                return redirect('items:category_manage')
    
    else:
        return redirect('for_admin:ad_login')    
    
    
def edit_categories(request,category_id):
    if request.user.is_superuser:
        if request.method == 'POST':
            category_name = request.POST.get('edit_name')
            category_image = request.FILES.get('edit_image')
            description = request.POST.get('edit_description')
            
            
             #---validate the form data-----

            if category_name.strip() == "":
                messages.error(request,"Field is empty!")
                return redirect('items:category_manage')
            elif Category.objects.filter(name=category_name).exclude(id=category_id).exists():
                messages.error(request, 'The category name is already taken')
                return redirect('items:category_manage')
            elif not category_image:
                messages.error(request, 'Image is not uploaded!')
                return redirect('items:category_manage')
            elif description.strip() == '':
                messages.error(request, 'Description is not given!')
                return redirect('items:category_manage')
    
            # Update the category instance
        
            update = get_object_or_404(Category,id=category_id)
            update.name = category_name
            update.image = category_image
            update.category_description = description
        
            update.save()
            messages.success(request, 'Category updated successfully')
            return redirect('items:category_manage')

    else:
        return redirect('for_admin:ad_login')



def delete_categories(request,category_id):
    if request.user.is_superuser:
        category = get_object_or_404(Category, id=category_id)
        category.delete()
        return redirect('items:category_manage')
    else:
        return redirect('for_admin:ad_login')
  
#BRAND----------------------------------------------------------------------------------  
  
    
def brand(request):
    brand = Brand.objects.all()
    print(brand)
    context = {
        'brand':brand
    }
    return render(request,'admini/brand.html',context)
    
  


def add_brand(request):
    if request.user.is_superuser:
        if request.method == 'POST' :
            brand_name   = request.POST.get('name')
            brand_image = request.FILES.get('image')
            # validating whether the field is empty
            
            if brand_name.strip() == '':
                messages.error(request, 'field is empty!')
                return redirect('items:add_brand')
            elif Brand.objects.filter(brand_name=brand_name).exists():
                messages.error(request, 'the brand is already taken')
                return redirect('items:add_brand')
            elif not brand_image:
                messages.error(request, 'image is not uploaded!')
                return redirect('items:add_brand')
            
            
            else:
                new_brand = Brand.objects.create(brand_name=brand_name,brand_image=brand_image)
                
                new_brand.save()
                messages.success(request, 'Brands are added successfully')
                return redirect('items:brand')
    
    else:
        return redirect('for_admin:ad_login')    
       
       
def edit_brand(request,brand_id):
    if request.user.is_superuser:
        if request.method == 'POST':
            brand_name = request.POST.get('edit_name')
            brand_image = request.FILES.get('edit_image')
            
            
            
            #---validate the form data-----

            if brand_name.strip() == "":
                messages.error(request,"Field is empty!")
                return redirect('items:brand')
            elif Brand.objects.filter(brand_name=brand_name).exclude(id=brand_id).exists():
                messages.error(request, 'The brand name is already taken')
                return redirect('items:brand')
            elif not brand_image:
                messages.error(request, 'Image is not uploaded!')
                return redirect('items:brand')
            
            # Update the brand instance
        
            update = get_object_or_404(Brand,id=brand_id)
            update.brand_name = brand_name
            update.brand_image = brand_image
            print(brand_name)
        
            update.save()
            messages.success(request, 'Brand updated successfully')
            return redirect('items:brand')
        else:
            return render(request,'items:brand')
    else:
        return redirect('for_admin:ad_login')
    
    
def delete_brand(request,brand_id):
    if request.user.is_superuser:
        brand = get_object_or_404(Brand, id=brand_id)
        brand.delete()
        return redirect('items:brand')
    else:
        return redirect('for_admin:ad_login')
    
   
#COLOR-----------------------------------------------------------------------------------   
   
   
    
def color(request):
    color = Color.objects.all()
    print(color)
    context = {
        'color':color
    }
    return render(request,'admini/color.html',context)



    
    

def add_color(request):
    if request.user.is_superuser:
        if request.method == 'POST' :
            color_name   = request.POST.get('name')
            # validating whether the field is empty
            
            if color_name.strip() == '':
                messages.error(request, 'field is empty!')
                return redirect('items:add_color')
            elif Color.objects.filter(name=color_name).exists():
                messages.error(request, 'the color is already taken')
                return redirect('items:color')
            
            
            
            else:
                new_color = Color.objects.create(name=color_name)
                
                new_color.save()
                messages.success(request, 'Colors are added successfully')
                return redirect('items:color')
    
        else:
            return render(request,'admini/color.html')
    else:
        return redirect('for_admin:ad_login')     
    
    
    
    
def edit_color(request,color_id):
    if request.user.is_superuser:
        if request.method == 'POST':
            color_name = request.POST.get('edit_name')
            
            
            
            
            #---validate the form data-----

            if color_name.strip() == "":
                messages.error(request,"Field is empty!")
                return redirect('items:color')
            elif Color.objects.filter(name=color_name).exclude(id=color_id).exists():
                messages.error(request, 'The color is already taken')
                return redirect('items:color')

            
            
            # Update the brand instance
        
            update = get_object_or_404(Color,id=color_id)
            update.name = color_name
            
            update.save()
            messages.success(request, 'Color updated successfully')
            return redirect('items:color')

    else:
        return redirect('for_admin:ad_login')
    
    
    
def delete_color(request,color_id):
    if request.user.is_superuser:
        color = get_object_or_404(Color, id=color_id)
        color.delete()
        return redirect('items:color')
    else:
        return redirect('for_admin:ad_login')
      

#SIZE-----------------------------------------------------------------------------------  



def size(request):
    size = Size.objects.all()
    print(size)
    context = {
        'size' : size
        
    }
    return render(request,'admini/size.html',context)


def add_size(request):
    if request.user.is_superuser:
        if request.method == 'POST' :
            size_name   = request.POST.get('name')
            
            # validating whether the field is empty
            
            if size_name.strip() == '':
                messages.error(request, 'field is empty!')
                return redirect('items:add_size')
            elif Size.objects.filter(name=size_name).exists():
                messages.error(request, 'This size is already taken')
                return redirect('items:size')
            
            
            
            else:
                new_size = Size.objects.create(name=size_name)
                
                new_size.save()
                messages.success(request, 'Sizes are added successfully')
                return redirect('items:size')
        else:
            # Render the form for a GET request
            return render(request, 'admini/size.html')
    else:
        return redirect('for_admin:ad_login')     
    


def edit_size(request,id):
    if request.user.is_superuser:
        if request.method == 'POST':
            name = request.POST.get('edit_name')
            
            
            #---validate the form data-----

            if name.strip() == "":
                messages.error(request,"Field is empty!")
                return redirect('items:size')
            elif Size.objects.filter(name=name).exclude(id=id).exists():
                messages.error(request, 'The size is already taken')
                return redirect('items:size')

            
            
            # Update the brand instance
        
            update = get_object_or_404(Size,id=id)
            update.name = name
            
            update.save()
            messages.success(request, 'Size updated successfully')
            return redirect('items:size')

    else:
        return redirect('for_admin:ad_login')
    
    
    
    
def delete_size(request,id):
    if request.user.is_superuser:
        size = get_object_or_404(Size, id=id)
        size.delete()
        return redirect('items:size')
    else:
        return redirect('for_admin:ad_login')
    
    
    
def product_manage(request):
    products = Products.objects.all()
    print(products)
    context = {
        'product' : products
        
    }
    return render(request,'admini/pro_manage.html',context)


def add_product(request):
    if request.user.is_superuser:
        category=Category.objects.all()
        brand=Brand.objects.all()
        size=Size.objects.all()
        color=Color.objects.all()
        context={   
            'category':category,
            'brand':brand,
            'size':size,
            'color':color
        }
        if request.method == "POST":
           
            name = request.POST['name']
            description = request.POST['description']
            brand_name = request.POST.get('brand')
            category_name = request.POST.get('category')
            color = request.POST.getlist('color')
            size = request.POST.getlist('size')
            price = request.POST['price']
            stock = request.POST['stock']
            images = request.POST.FILES.getlist('image')
            
            if not name or not description or not brand_name or not category_name or not color or not size or not price or not stock:
                messages.error(request, 'Fields cannot be empty')
                return redirect('items:add_product')
            
            else:
                brand, created = Brand.objects.get_or_create(brand_name=brand_name)
                category, created = Category.objects.get_or_create(category_name=category_name)
                
                product = Products.objects.create(
                    name=name,
                    description=description,
                    brand=brand,
                    category=category,
                    price=price,
                    stock=stock
                )
                
                product.colors.set(Color.objects.filter(id__in=color))
                product.size.set(Size.objects.filter(id__in=size))
                product.save()
                
            for image in images:
                print("image to save", image)
                product_image = product_image(product=product,image=image)
                print("image to save:", product_image)
                product_image.save()
                
            return redirect('items:product_manage')
        
        else:
            return render(request, 'admini/product/add_pro.html',context)
                
            
    else:   
        return redirect('for_admin:ad_login')
    
    
    
   