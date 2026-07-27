from django.http import HttpResponse

def pagina_teste(request):
    return HttpResponse("<h1>Funcionando! 🎉</h1><p>Django rodando com sucesso.</p>")