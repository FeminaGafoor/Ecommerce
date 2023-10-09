from django.urls import path
from . import views

app_name='categories'

urlpatterns = [
    path('categories/',views.categories,name='categories'),
    path('mens/',views.mens,name='mens'),
    path('kids/',views.kids,name='kids'),
]