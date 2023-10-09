from django.urls import path
from . import views

app_name='outgoing'


urlpatterns = [
    path('shipping_address/',views.shipping_address,name='shipping_address'),
    path('payments',views.payments,name='payments'),
    path('summary',views.summary,name='summary'),
    path('finish',views.finish,name='finish'),
]
    