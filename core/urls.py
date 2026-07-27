from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('sales/', views.sales, name='sales'),
    path('stock/', views.stock, name='stock'),
    path('control/', views.control, name='control'),
]