from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')

def sales(request):
    return render(request, 'core/sales.html')

def stock(request):
    return render(request, 'core/stock.html')

def control(request):
    return render(request, 'core/control.html')