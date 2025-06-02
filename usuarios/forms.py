from django import forms
from .models import Usuario, Direccion
from pedidos.models import MetodoPago
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User

class DireccionForm(forms.ModelForm):
    class Meta:
        model = Direccion
        fields = ['direccion','telefono','ciudad','pais','codigo_postal','es_default']

class MetodoPagoForm(forms.ModelForm):
    class Meta:
        model = MetodoPago
        fields = ['nombre','descripcion']




















class RegistroForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = Usuario
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Nombre de usuario'
        self.fields['email'].label = 'Correo electrónico'
        self.fields['password1'].label = 'Contraseña'
        self.fields['password2'].label = 'Confirmar contraseña'
        self.fields['username'].help_text = 'Este será tu identificador único.'
        self.fields['password1'].help_text = 'La contraseña debe tener al menos 8 caracteres.'
        self.fields['password2'].help_text = 'Confirma tu contraseña.'
        self.fields['username'].widget.attrs.update({'placeholder': 'Ej: juan123'})
        self.fields['email'].widget.attrs.update({'placeholder': 'ejemplo@dominio.com'})
        self.fields['password1'].widget.attrs.update({'placeholder': '********'})
        self.fields['password2'].widget.attrs.update({'placeholder': '********'})

class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Nombre de usuario'
        self.fields['password'].label = 'Contraseña'
        self.fields['username'].help_text = 'Introduce tu nombre de usuario.'
        self.fields['password'].help_text = 'Introduce tu contraseña.'
        self.fields['username'].widget.attrs.update({'placeholder': 'Ej: juan123'})
        self.fields['password'].widget.attrs.update({'placeholder': '********'})

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('username', 'email') 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Nombre de usuario'
        self.fields['email'].label = 'Correo electrónico' 
        self.fields['username'].widget.attrs.update({'placeholder': 'Ej: juan123'})
        self.fields['email'].widget.attrs.update({'placeholder': 'ejemplo@dominio.com'})
        self.fields['email'].validators.append(self.unique_email_validator) 
    def unique_email_validator(self, email):
        if Usuario.objects.exclude(id=self.instance.id).filter(email=email).exists():
            raise forms.ValidationError("Este correo electrónico ya está registrado.")

class PasswordChangeForm(PasswordChangeForm):
    password_actual = forms.CharField(
        label="Contraseña actual",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        error_messages={'required': 'Este campo es obligatorio.'}
    )
    nueva_password1 = forms.CharField(
        label="Nueva contraseña",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text="La contraseña debe tener al menos 8 caracteres.",
        error_messages={'required': 'Este campo es obligatorio.'}
    )
    nueva_password2 = forms.CharField(
        label="Confirmar nueva contraseña",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        error_messages={'required': 'Este campo es obligatorio.'}
    )