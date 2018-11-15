from django import forms
from django.core.exceptions import ValidationError
from apps.language.models import Language


class LanguageForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(LanguageForm, self).__init__(*args, **kwargs)
        self.fields['name'].required = False
        self.fields['level'].required = False

    class Meta:

        model = Language

        fields = [
            'name', 'level'
        ]

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Idioma',
                }),
            'level': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'nivel',
                }),
        }

    def clean_name(self):
        data = self.cleaned_data
        if not data['name']:
            raise ValidationError('El campo idioma esta vació')
        return data['name']

    def clean_level(self):
        data = self.cleaned_data
        if not data['level']:
            raise ValidationError('El campo nivel esta vació')
        return data['level']
