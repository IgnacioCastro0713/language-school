from django import forms
from apps.classroom.models import Classroom
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class ClassroomForm(forms.ModelForm):

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
                }
            ),
        }
