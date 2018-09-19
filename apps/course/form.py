from django import forms
from apps.course.models import Course, User


class CourseForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CourseForm, self).__init__(*args, **kwargs)
        self.fields['user'].queryset = User.objects.filter(role__reference__exact='teacher')
        self.fields['lan'].empty_label = None

    class Meta:
        model = Course

        DAYS = (
            ('lunes', 'Lunes'),
            ('martes', 'Martes'),
            ('miercoles', 'Miercoles'),
            ('jueves', 'Jueves'),
            ('viernes', 'Viernes'),
        )

        TIME = (
            ('08:00:00', '8:00 am'),
            ('09:00:00', '9:00 am'),
            ('10:00:00', '10:00 am'),
            ('11:00:00', '11:00 am'),
            ('12:00:00', '12:00 pm'),
            ('13:00:00', '1:00 pm'),
            ('14:00:00', '2:00 pm'),
            ('15:00:00', '3:00 pm'),
            ('16:00:00', '4:00 pm'),
            ('17:00:00', '5:00 pm'),
            ('18:00:00', '6:00 pm'),
        )

        fields = [
            'name',
            'day',
            'start',
            'end',
            'description',
            'user',
            'classroom',
            'lan',
        ]
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre curso',
                }),
            'day': forms.Select(
                choices=DAYS,
                attrs={
                    'class': 'form-control',
                }
            ),
            'start': forms.Select(
                choices=TIME,
                attrs={
                    'class': 'form-control',
                }),
            'end': forms.Select(
                choices=TIME,
                attrs={
                    'class': 'form-control',
                }),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                }),
            'user': forms.SelectMultiple(
                attrs={
                    'class': 'form-control',
                }),
            'classroom': forms.SelectMultiple(
                attrs={
                    'class': 'form-control',
                }),
            'lan': forms.Select(
                attrs={
                    'class': 'form-control',
                }),
        }
