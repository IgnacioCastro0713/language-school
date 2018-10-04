from django import forms
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError
from apps.user.backends import CustomBackendUser as Auth
from django.contrib.auth.forms import (
    PasswordResetForm,
    SetPasswordForm,
    AuthenticationForm,
    UsernameField,
)


class ResetForm(PasswordResetForm):
    email = forms.EmailField(max_length=254, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Correo electrónico'
    }))


class ResetConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nueva contraseña'
        }),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirmar contraseña'
        }),
    )


class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].required = False
        self.fields['password'].required = False

    username = UsernameField(widget=forms.TextInput(
        attrs={
            'autofocus': True,
            'class': 'form-control',
            'placeholder': 'Codigo...'
        }))
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Contraseña'
        }))

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username is not None and password:
            self.user_cache = Auth.authenticate(username=username, password=password)
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data

    def clean_username(self):
        data = self.cleaned_data
        if not data['username']:
            raise ValidationError('El campo código esta vacio')
        return data['username']

    def clean_password(self):
        data = self.cleaned_data
        if not data['password']:
            raise ValidationError('El campo contraseña esta vacio')
        return data['password']
