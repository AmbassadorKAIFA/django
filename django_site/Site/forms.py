from django import forms

from django.contrib.auth.forms import UserCreationForm

from .models import *

class CreateTableDataForm(forms.ModelForm):
    class Meta:
        model = Table
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }


class DateInput(forms.DateInput):
    input_type = 'date'


class DateInputTableForm(forms.Form):
    date = forms.DateField(widget=DateInput)


class MyUserCreationForm(UserCreationForm):

    class Meta:
        model = MyUser
        fields = ('username', 'password1', 'password2')


class TableBookingForm(forms.ModelForm):
    class Meta:
        model = Table
        fields = ('booking', )


class AppointmentForm(forms.Form):
    name = forms.CharField(max_length=100, min_length=2)
    email = forms.EmailField(max_length=150, min_length=4, help_text='Укажите действующий Email')