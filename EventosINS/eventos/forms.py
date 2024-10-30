# eventos/forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm, SetPasswordForm

class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Correo electrónico',
        'class': 'input-field'  # Aplica la clase de estilo al campo de correo electrónico
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Contraseña',
        'class': 'input-field'  # Aplica la clase de estilo al campo de contraseña
    }))

# Formulario personalizado para restablecer la contraseña
class CustomSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'input-field', 
            'placeholder': 'Nueva Contraseña'
        })
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'input-field', 
            'placeholder': 'Confirmar Contraseña'
        })
    )
