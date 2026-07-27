from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Projeto Django rodando com sucesso no Render!</h1>")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')), # <--- Isto direciona para o seu app core
]