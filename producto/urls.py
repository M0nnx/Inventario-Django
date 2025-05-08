from django.urls import path
from . import views
from .views import VerProductos,CrearProductos,EditarProductos,BorrarProductos,VerProductoPorId,CrearCategorias,ProductoCategoria,BorrarCategoria,EditarCategoria,Dashboard

urlpatterns = [
    #Administracion
    path('dashboard/', Dashboard.as_view(), name='dashboard'),


    #Categoria
    path('crearC/', CrearCategorias.as_view(), name='crearCategoria'),
    path('categorias/<int:categoria_id>/', ProductoCategoria.as_view(), name='verxCategorias'),
    path('borrarC/<int:pk>/', BorrarCategoria.as_view(), name='borrarCategorias'),
    path('editarC/<int:pk>/', EditarCategoria.as_view(), name='editarCategorias'),

    #Productos
    path('crear/', CrearProductos.as_view(), name='crearProducto'),
    path('editar/<int:pk>/', EditarProductos.as_view(), name='editarProducto'),
    path('borrar/<int:pk>/', BorrarProductos.as_view(), name='borrarProducto'),
    path('detalle/<int:pk>', VerProductoPorId.as_view(), name='verProductoId'),
    path('ver/', VerProductos.as_view(), name='verProducto'),

]
