from django import forms
from apps.user.models import User


class UserForm(forms.ModelForm):

    class Meta:

        model = User

        fields = [
            'code',
            'password',
            'first_name',
            'last_name',
            'second_last_name',
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
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'txtnombre',
                'placeholder': 'Nombre',
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'txtapaterno',
                'placeholder': 'Apellido paterno',
            }),
            'second_last_name': forms.TextInput(attrs={
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
                'class': 'form-check-input',
                'id': 'role',
            })
        }
