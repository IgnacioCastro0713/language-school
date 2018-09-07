from django import forms
from apps.user.models import User


class UserForm(forms.ModelForm):
    class Meta:

        model = User

        fields = [
            'code',
            'password',
            'nombre',
            'apaterno',
            'amaterno',
            'email',
            'address',
            'phone',
            'role',
        ]
        widgets = {
            'code': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'txtcode',
                'placeholder': 'Código',
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control',
                'id': 'txtpass',
                'placeholder': 'Contraseña',
            }),
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'txtnombre',
                'placeholder': 'Nombre',
            }),
            'apaterno': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'txtapaterno',
                'placeholder': 'Apellido paterno',
            }),
            'amaterno': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'txtamaterno',
                'placeholder': 'Apellido materno',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'id': 'txtxemail',
                'placeholder': 'Correo electrónico',
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'txtaddress',
                'placeholder': 'Dirección',
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'txtphone',
                'placeholder': 'Telefono',
            }),
            'role': forms.RadioSelect(attrs={
                'class': 'form-control',
                'id': 'role'
            })
        }
