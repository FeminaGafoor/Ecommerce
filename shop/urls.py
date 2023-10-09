from django.urls import path
from . import views

app_name='shop'

urlpatterns = [
    path('shop/',views.shop,name='shop'),
    path('product/',views.product,name='product'),
]
    