from django import forms
from apps.course.models import Course, User, DAYS


class CourseForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):  # Function to filter users type teachers
        super(CourseForm, self).__init__(*args, **kwargs)
        self.fields['user'].queryset = User.objects.filter(role__reference__exact='teacher')

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
            'user',
        ]

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre curso',
            }),
            'day': forms.Select(
                choices=DAYS,
                attrs={
                    'class': 'form-control',
                }
            ),
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
                'class': 'form-control'
            }),
            'classroom': forms.Select(attrs={
                'class': 'form-select-input'
            }),
            'user': forms.Select(attrs={
                'class': 'form-control'
            }),
        }
