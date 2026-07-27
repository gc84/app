from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')

def sales(request):
    return render(request, 'core/templates/core/sales.html')

def stock(request):
    return render(request, 'core/templates/core/stock.html')

def control(request):
    return render(request, 'core/templates/core/control.html')