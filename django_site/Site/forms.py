from django import forms

from .models import *

class CreateTableDataForm(forms.ModelForm):
    class Meta:
        model = Table
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }


class DateForm(forms.Form):
    date = forms.DateTimeField(
        input_formats=['%d/%m/%Y'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        })
    )


class DateInputTableForm(forms.Form):
    date = forms.DateField(input_formats='%Y-%m-%d')


class TableBookingForm(forms.ModelForm):
    class Meta:
        model = Table
        fields = ('booking', )