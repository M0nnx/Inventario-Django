from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('editar/<int:pk>/', views.actualizarProducto, name='actualizarProducto'),
]
