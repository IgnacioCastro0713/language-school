from django import forms
from apps.course.models import Course


class CourseForm(forms.ModelForm):
    class Meta:

        model = Course

        fields = [
            'name',
            'day',
            'start',
            'end',
            'description',
            'language',
            'classroom',
            'user'
        ]
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre curso',
            }),
            'day': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Día',
            }),
            'start': forms.TimeInput(attrs={
                'class': 'form-control',
            }),
            'end': forms.TimeInput(attrs={
                'class': 'form-control',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
            }),
            'language': forms.Select(attrs={
                'class': 'form-select-input'
            }),
            'classroom': forms.Select(attrs={
                'class': 'form-select-input'
            }),
            'user': forms.Select(attrs={
                'class': 'form-select-input'
            }),
        }
