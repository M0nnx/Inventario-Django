from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductoForm, CategoriaForm
from .models import Producto, Categoria
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView, UpdateView,DeleteView, DetailView
from django.urls import reverse_lazy
import cloudinary.uploader

class CrearProductos(LoginRequiredMixin, UserPassesTestMixin,CreateView):
    model = Producto
    template_name = 'productos/crearProducto.html'
    form_class = ProductoForm
    success_url = reverse_lazy('dashboard')
    def test_func(self):
        return self.request.user.groups.filter(name='Administrador').exists()
    def handle_no_permission(self):
        messages.error(self.request, "No tienes permisos para acceder a esta página.")
        return redirect('home')
    def form_valid(self, form):
        producto = form.save(commit=False)
        producto.save()
        imagen = form.cleaned_data.get('imagen')
        if imagen:
            folder_path = f'productoD/{producto.nombre}_{producto.id}/'
            resultado = cloudinary.uploader.upload(
                imagen,
                folder=folder_path
            )
            producto.imagen_url = resultado['secure_url']
            producto.save() 

        return super().form_valid(form)
class EditarProductos(LoginRequiredMixin, UserPassesTestMixin,UpdateView):
    model = Producto
    template_name = 'productos/editarProducto.html'
    form_class = ProductoForm
    context_object_name = 'producto'
    success_url = reverse_lazy('dashboard')
    def test_func(self):
        return self.request.user.groups.filter(name='Administrador').exists()
    def handle_no_permission(self):
        messages.error(self.request, "No tienes permisos para acceder a esta página.")
        return redirect('home')

    def form_valid(self, form):
        producto = form.save(commit=False)
        imagen = form.cleaned_data.get('imagen')
        if imagen:
            folder_path = f'productoD/{producto.nombre}_{producto.id}/'
            resultado = cloudinary.uploader.upload(
                imagen,
                folder=folder_path
            )
            producto.imagen_url = resultado['secure_url']
        producto.save()
        return super().form_valid(form)


class BorrarProductos(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
    model = Producto
    template_name = 'productos/borrarProducto.html'
    success_url = reverse_lazy('dashboard')
    def test_func(self):
        return self.request.user.groups.filter(name='Administrador').exists()
    def handle_no_permission(self):
        messages.error(self.request, "No tienes permisos para acceder a esta página.")
        return redirect('home')
class VerProductos(ListView):
    model = Producto
    template_name = 'productos/listaProducto.html'
    context_object_name = 'productos'
    success_url = reverse_lazy('dashboard')
class VerProductoPorId(DetailView):
    model = Producto
    template_name = 'productos/detalleProducto.html'
    context_object_name = 'producto'

class CrearCategorias(LoginRequiredMixin, UserPassesTestMixin,CreateView):
    model = Categoria
    template_name = 'productos/crearCategoria.html'
    form_class = CategoriaForm
    success_url = reverse_lazy('dashboard')
    def test_func(self):
        return self.request.user.groups.filter(name='Administrador').exists()
    def handle_no_permission(self):
        messages.error(self.request, "No tienes permisos para acceder a esta página.")
        return redirect('home')
    def form_valid(self, form):
        imagen = form.cleaned_data.get('imagen')
        self.object = form.save(commit=False)
        
        if imagen:
            resultado = cloudinary.uploader.upload(
                imagen,
                folder=f"categoria/{form.cleaned_data['nombre']}"
            )
            self.object.imagen_url = resultado.get('secure_url')
        
        self.object.save()
        return super().form_valid(form)
class Dashboard(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Producto
    template_name = 'productos/dashboard.html'
    context_object_name = 'productos'
    def test_func(self):
        return self.request.user.groups.filter(name='Administrador').exists()
    def handle_no_permission(self):
        messages.error(self.request, "No tienes permisos para acceder a esta página.")
        return redirect('home')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        productos = context['productos']
        total = sum(producto.precio for producto in productos)
        producto_stock_bajo = min(
            productos, key=lambda p: p.stock, default=None
        ) if productos else None
        if producto_stock_bajo and producto_stock_bajo.stock >= 15:
            producto_stock_bajo = None
        context['total'] = total
        context['producto_stock_bajo'] = producto_stock_bajo
        return context

class ProductoCategoria(ListView):
    model = Producto
    template_name= 'productos/categorias.html'
    context_object_name = 'productos'

    def get_queryset(self):
        categoria_id = self.kwargs['categoria_id']
        return Producto.objects.filter(categoria__id=categoria_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categoria_id = self.kwargs['categoria_id']
        categoria = Categoria.objects.get(id=categoria_id)
        context['categoria'] = categoria
        return context
