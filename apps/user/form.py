from django import forms
from apps.user.models import User


class FormUser(forms.ModelForm):
    class Meta:

        model = User

        fields = [
            'code',
            'nombre',
            'apaterno',
            'amaterno',
            'email',
            'address',
            'phone',
        ]
        widgets = {
            'code': forms.TextInput(attrs={
                'class': 'clase_css',
                'id': 'id_name',
                'name': 'name_name',
                'placeholder': 'Código...'
            }),
            'nombre': forms.TextInput(attrs={
                'class': 'clase_css',
                'id': 'id_name',
                'name': 'name_name',
            }),
            'apaterno': forms.TextInput(attrs={
                'class': 'clase_css',
                'id': 'id_name',
                'name': 'name_name',
            }),
            'amaterno': forms.TextInput(attrs={
                'class': 'clase_css',
                'id': 'id_name',
                'name': 'name_name',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'clase_css',
                'id': 'id_name',
                'name': 'name_name',
            }),
            'address': forms.TextInput(attrs={
                'class': 'clase_css',
                'id': 'id_name',
                'name': 'name_name',
            }),
            'phone': forms.TextInput(attrs={
                'class': 'clase_css',
                'id': 'id_name',
                'name': 'name_name',
            }),
        }
