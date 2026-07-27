from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from . import views

def home(request):
    return HttpResponse("<h1>Projeto Django rodando com sucesso no Render!</h1>")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('sales/', views.sales, name='sales'),
    path('stock/', views.stock, name='stock'),
    path('control/', views.control, name='control'),
]