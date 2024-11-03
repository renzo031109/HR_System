from django import forms
from django.forms import modelformset_factory
from .models import Staff_Record

class ReceivedForm(forms.ModelForm):

    class Meta:

        model = Staff_Record

        fields = [
            'employee_id',
            'last_name',
            'first_name',
            'department',
            'client'
        ]

        labels = {
            'employee_id': 'EMPLOYEE ID',
            'last_name' : 'LAST NAME',
            'first_name' : 'FIRST NAME',
            'department' : 'DEPARTMENT',
            'client' : 'CLIENT'
        }

        widgets = {

            'employee_id': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder': '0',
                'autocomplete': 'off',
                'required':True
            }),
            'last_name': forms.TextInput(attrs={
                'class':'form-control',
                'autocomplete': 'off',
                'required':True
            }),
            'first_name': forms.TextInput(attrs={
                'class':'form-control',
                'autocomplete': 'off',
                'required':True
            }),
            'department': forms.Select(attrs={
                'class':'form-control', 
            }),
            'client': forms.Select(attrs={
                'class':'form-control', 
            }),

        }

# modelformset functions
ReceivedFormSet = modelformset_factory(Staff_Record, form=ReceivedForm, extra=1) 

