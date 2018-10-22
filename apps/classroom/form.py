from django import forms
from django.core.exceptions import ValidationError
from apps.classroom.models import Classroom


class ClassroomForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ClassroomForm, self).__init__(*args, **kwargs)
        self.fields['name'].required = False
        self.fields['building'].required = False

    class Meta:

        model = Classroom

        fields = [
            'name', 'building'
        ]

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre de aula',
                }),
            'building': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'nombre edificio',
                }),
        }

    def clean_name(self):
        data = self.cleaned_data
        if not data['name']:
            raise ValidationError('El campo nombre esta vació')
        return data['name']

    def clean_building(self):
        data = self.cleaned_data
        if not data['building']:
            raise ValidationError('El campo edificio esta vació')
        return data['building']
