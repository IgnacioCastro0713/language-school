from django import forms
from django.core.exceptions import ValidationError

from apps.user.models import User


class UserForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['role'].empty_label = None

        self.fields['code'].required = False
        self.fields['password'].required = False
        self.fields['first_name'].required = False
        self.fields['last_name'].required = False
        self.fields['second_last_name'].required = False
        self.fields['email'].required = False
        self.fields['address'].required = False
        self.fields['phone'].required = False
        self.fields['role'].required = False

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

    def clean_code(self):
        data = self.cleaned_data
        if not data['code']:
            raise ValidationError('El campo código esta vacio')
        return data['code']

    def clean_password(self):
        data = self.cleaned_data
        if not data['password']:
            raise ValidationError('El campo contraseña esta vacio')
        return data['password']

    def clean_email(self):
        data = self.cleaned_data
        if not data['email']:
            raise ValidationError('El campo correo electronico esta vacio')
        return data['email']
