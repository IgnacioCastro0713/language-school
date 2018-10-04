from django import forms
from apps.classroom.models import Classroom


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
