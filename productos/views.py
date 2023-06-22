from django.shortcuts import render
from .models import Marca, Talla, Producto
# Create your views here.

def index(request):
    context={}
    return render(request, 'productos/index.html',context)

def productosList(request):
    productos = Producto.objects.all()
    context={
        'productos' : productos
    }
    return render(request, 'productos/productosList.html',context)