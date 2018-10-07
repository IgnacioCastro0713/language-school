from django import forms
from django.core.exceptions import ValidationError

from apps.course.models import Course, User


class CourseForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CourseForm, self).__init__(*args, **kwargs)
        self.fields['user'].queryset = User.objects.filter(role__reference__exact='teacher')
        self.fields['lan'].empty_label = '-- Seleciona idioma y nivel --'
        self.fields['classroom'].empty_label = '-- Seleciona aula --'
        # required fields false
        self.fields['name'].required = False
        self.fields['description'].required = False
        self.fields['day'].required = False
        self.fields['start'].required = False
        self.fields['end'].required = False

    class Meta:
        model = Course

        DAYS = (
            ('', '--Selecciona un día--'),
            ('lunes', 'Lunes'),
            ('martes', 'Martes'),
            ('miercoles', 'Miércoles'),
            ('jueves', 'Jueves'),
            ('viernes', 'Viernes'),
        )

        TIME = (
            ('', 'Selecciona'),
            ('08:00:00', '8:00 a.m.'),
            ('09:00:00', '9:00 a.m.'),
            ('10:00:00', '10:00 a.m.'),
            ('11:00:00', '11:00 a.m.'),
            ('12:00:00', '12:00 p.m.'),
            ('13:00:00', '1:00 p.m.'),
            ('14:00:00', '2:00 p.m.'),
            ('15:00:00', '3:00 p.m.'),
            ('16:00:00', '4:00 p.m.'),
            ('17:00:00', '5:00 p.m.'),
            ('18:00:00', '6:00 p.m.'),
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
            'classroom': forms.Select(
                attrs={
                    'class': 'form-control',
                }),
            'lan': forms.Select(
                attrs={
                    'class': 'form-control',
                }),
        }

    def clean_name(self):
        data = self.cleaned_data
        if not data['name']:
            raise ValidationError('El campo nombre esta vació')
        return data['name']

    def clean_lan(self):
        data = self.cleaned_data
        if not data['lan']:
            raise ValidationError('Debe selecionar idioma y nivel')
        return data['lan']

    def clean_user(self):
        data = self.cleaned_data
        if not data['user']:
            raise ValidationError('Debe selecionar un profesor')
        if len(data['user']) > 1:
            raise ValidationError('Debe selecionar solo un profesor')
        return data['user']

    def clean_day(self):
        data = self.cleaned_data
        if not data['day']:
            raise ValidationError('Debe selecionar un día')
        return data['day']

    def clean_start(self):
        data = self.cleaned_data
        if not data['start']:
            raise ValidationError('Selecciona hora de inicio')
        return data['start']

    def clean_end(self):
        data = self.cleaned_data
        if not data['end']:
            raise ValidationError('Selecciona hora de fin')
        return data['end']

    def clean_classroom(self):
        data = self.cleaned_data
        if not data['classroom']:
            raise ValidationError('Debe selecionar un aula')
        return data['classroom']

    def clean_description(self):
        data = self.cleaned_data
        if not data['description']:
            raise ValidationError('El campo decripción esta vació')
        return data['description']

