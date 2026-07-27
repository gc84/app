from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

# Opcional: uma view simples para a raiz "/" não dar Not Found
def home(request):
    return HttpResponse("<h1>Projeto Django rodando com sucesso no Render!</h1>")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home), # Mostra essa mensagem na página inicial
]