from django.shortcuts import redirect, render
from .models import Marca, Talla, Producto
from .forms import ProductoForm
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

def productosAdd(request):
    context= {'form': ProductoForm()}
    #verificar peticion Post
    if request.method=='POST':
        #con el request se recuperan los datos del form
        formulario=ProductoForm(request.POST, files=request.FILES)
        if formulario.is_valid:
            formulario.save()
            context={'mensaje':"Producto guardado correctamente"}
    return render(request, 'productos/productosAdd.html', context)

def productosEdit(request, pk):
    # Select * from alumnos where id_prod=pk
    producto=Producto.objects.get(id_prod=pk)

    context= {'form': ProductoForm(instance=producto)}
    #verificar peticion Post
    if request.method=='POST':
        #con el request se recuperan los datos del form
        # se filtra por el id del producto a editar
        formulario=ProductoForm(request.POST, files=request.FILES, instance=producto)
        if formulario.is_valid:
            formulario.save()
            context={'mensaje':"Producto se edito correctamente"}
    return render(request, 'productos/productosAdd.html', context)

def productosDel(request,pk):
    producto=Producto.objects.get(id_prod=pk)
    producto.delete()
    return redirect(to='productosList')