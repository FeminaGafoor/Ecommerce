from django.urls import path
from . import views

app_name='items'

urlpatterns = [

    path('category_manage/',views.category_manage,name='category_manage'),
    path('add_categories/',views.add_categories,name='add_categories'),
    path('edit_categories/<int:category_id>',views.edit_categories,name='edit_categories'),
    path('delete_categories/<int:category_id>',views.delete_categories,name='delete_categories'),
    path('brand/',views.brand,name='brand'),
    path('add_brand/',views.add_brand,name='add_brand'),
    path('edit_brand/<int:brand_id>',views.edit_brand,name='edit_brand'),
    path('delete_brand/<int:brand_id>',views.delete_brand,name='delete_brand'),
    path('color/',views.color,name='color'),
    path('add_color/',views.add_color,name='add_color'),
    path('edit_color/<int:color_id>',views.edit_color,name='edit_color'),
    path('delete_color/<int:color_id>',views.delete_color,name='delete_color'),
    path('size/',views.size,name='size'),
    path('add_size/',views.add_size,name='add_size'),
    path('edit_size/<int:id>',views.edit_size,name='edit_size'),
    path('delete_size/<int:id>',views.delete_size,name='delete_size'),
    path('product_manage/',views.product_manage,name='product_manage'),
    path('add_product/',views.add_product,name='add_product'),
   
   
]