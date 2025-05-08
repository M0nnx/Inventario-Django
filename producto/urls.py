from django.urls import path
from . import views
from .views import VerProductos,CrearProductos,EditarProductos,BorrarProductos,Dashboard,VerProductoPorId,CrearCategorias,ProductoCategoria

urlpatterns = [
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('crear/', CrearProductos.as_view(), name='crearProducto'),
    path('editar/<int:pk>/', EditarProductos.as_view(), name='editarProducto'),
    path('borrar/<int:pk>/', BorrarProductos.as_view(), name='borrarProducto'),
    path('ver/', VerProductos.as_view(), name='verProducto'),
    path('detalle/<int:pk>', VerProductoPorId.as_view(), name='verProductoId'),

    #Categoria
    path('crearC/', CrearCategorias.as_view(), name='crearCategoria'),
    path('categorias/<int:categoria_id>/', ProductoCategoria.as_view(), name='verxCategorias'),

]
