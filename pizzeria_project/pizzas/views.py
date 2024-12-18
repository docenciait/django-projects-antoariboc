from django.shortcuts import render

# Create your views here.

def index(request):
    """Pagina principal para Pizzas"""
    return render(request, 'pizzas/index.html')

def example(request):
    """Pagina pexample"""
    return render(request, 'pizzas/example.html')