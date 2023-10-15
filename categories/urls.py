from django.urls import path
from . import views

app_name='categories'

urlpatterns = [

    path('category_manage/',views.category_manage,name='category_manage'),
    path('add_categories/',views.add_categories,name='add_categories'),
   
   
]