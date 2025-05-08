from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from usuarios.views import InicioSesionView,DesconectarView,PerfilView, RegistroUsuarioView, CustomPasswordChangeView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('registro/', RegistroUsuarioView.as_view(), name='registro'),
    path('login/', InicioSesionView.as_view(), name='login'),
    path('logout/', DesconectarView.as_view(), name='salir'),
    path('perfil/', PerfilView.as_view(), name='perfil'),
    path('cambiarContraseña/', CustomPasswordChangeView.as_view(), name='cambiarContraseña'),

    path('cambiarContraseña/hecho/', auth_views.PasswordChangeDoneView.as_view(), name='contraseñaCambiada'),
    path('recuperar-contraseña/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('recuperar-contraseña/hecho/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('restablecer-contraseña/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('contraseña-restablecida/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),


]
