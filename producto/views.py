from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductoForm, CategoriaForm
from .models import Producto, Categoria

def dashboard(request):
    productos = Producto.objects.all()
    categorias = Categoria.objects.all()

    productoForm = ProductoForm()
    categoriaForm = CategoriaForm()

    if request.method == 'POST':
        if 'submit_producto' in request.POST:
            productoForm = ProductoForm(request.POST)
            if productoForm.is_valid():
                productoForm.save()
                return redirect('dashboard')

        elif 'submit_categoria' in request.POST:
            categoriaForm = CategoriaForm(request.POST)
            if categoriaForm.is_valid():
                categoriaForm.save()
                return redirect('dashboard')

    context = {
        'productoForm': productoForm,
        'categoriaForm': categoriaForm,
        'productos': productos,
        'categorias': categorias,
    }
    return render(request, 'producto/dashboard.html', context)

def actualizarProducto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    form = ProductoForm(instance=producto)

    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    return render(request, 'producto/editarProducto.html', {'productoForm': form })