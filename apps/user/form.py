from django import forms
from django.core.exceptions import ValidationError

from apps.user.models import User


class UserForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = False
        self.fields['password'].required = False

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

    def clean_email(self):
        data = self.cleaned_data
        if User.objects.filter(email=data['email']).exists():
            raise ValidationError("Ya existe un usuario con este correo electrónico")
        if not data['email']:
            raise ValidationError('Este campo es obligatorio')
        return data

    def clean_password(self):
        data = self.cleaned_data
        if not data['password']:
            raise ValidationError('Este campo es obligatorio')
        return data
