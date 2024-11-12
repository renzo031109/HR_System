from django import forms
from django.forms import modelformset_factory
from .models import Employee_Record

class ReceivedForm(forms.ModelForm):

    class Meta:

        model = Employee_Record

        fields = [
            'employee_id',
            'last_name',
            'first_name',
            'department',
            'client',
            'component',
            'others'
        ]

        labels = {
            'employee_id': 'EMPLOYEE ID',
            'last_name' : 'LAST NAME',
            'first_name' : 'FIRST NAME',
            'department' : 'DEPARTMENT',
            'client' : 'CLIENT',
            'component' : 'ITEM',
            'others': 'OTHERS'
        }

        widgets = {

            'employee_id': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder': 'XXXXXX',
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
                'required':True
            }),
            'component': forms.Select(attrs={
                'class':'form-control', 
                'required':True,
            }),
            'others': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder': '*** Type here if not found in the description ***',
                'autocomplete': 'off',
            }),


        }

# modelformset functions
ReceivedModelFormSet = modelformset_factory(Employee_Record, form=ReceivedForm, extra=1) 

