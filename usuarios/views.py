from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import redirect
from .forms import RegistroForm, PerfilForm, CustomAuthenticationForm, PasswordChangeForm

class RegistroUsuarioView(CreateView):
    form_class = RegistroForm
    template_name = 'usuarios/registro.html'
    success_url = reverse_lazy('perfil')

    def form_valid(self, form):
        user = form.save()
        cliente_group = Group.objects.get(name='Clientes')
        user.groups.add(cliente_group)
        user.save()
        login(self.request, user)
        return redirect(self.success_url)

class InicioSesionView(LoginView):
    template_name = 'usuarios/login.html'
    authentication_form = CustomAuthenticationForm 
    redirect_authenticated_user = True

class DesconectarView(LogoutView):
    next_page = reverse_lazy('login')
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

class PerfilView(LoginRequiredMixin, UpdateView):
    form_class = PerfilForm
    template_name = 'usuarios/perfil.html'
    success_url = reverse_lazy('perfil')
    login_url = reverse_lazy('login')

    def get_object(self):
        return self.request.user

class CustomPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'usuarios/cambioPasswordForm.html' 
    success_url = reverse_lazy('perfil')
    form_class = PasswordChangeForm
