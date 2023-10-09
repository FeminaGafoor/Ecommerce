from django.urls import path
from . import views

app_name='for_admin'

urlpatterns = [
    path('admin_panel/',views.admin_panel,name='admin_panel'),
  
]