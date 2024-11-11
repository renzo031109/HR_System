import django_filters
from django_filters import DateFilter, CharFilter, ChoiceFilter
from .models import Employee_Record, Department, Client, Component
from django import forms


#department list
department = Department.objects.all()
department_list = []
for value in department:
    department_list.append((value.id, value.department))


#client list
client = Client.objects.all()
client_list = []
for value in client:
    client_list.append((value.id, value.client))


#component list
component = Component.objects.all()
component_list = []
for value in component:
    component_list.append((value.id, value.component))


#date filter class
class DateInput(forms.DateInput):
    input_type = 'date'


class EmployeeRecordFilter(django_filters.FilterSet):
    employee_id = CharFilter(field_name='employee_id', lookup_expr='icontains', label="EMPLOYEE ID")
    first_name = CharFilter(field_name='first_name', lookup_expr='icontains', label="FIRST NAME")
    last_name = CharFilter(field_name='last_name', lookup_expr='icontains', label="LAST NAME")
    department = ChoiceFilter(field_name='department', label="DEPARTMENT", choices=department_list)
    client = ChoiceFilter(field_name='client', label="CLIENT", choices=client_list)
    component = ChoiceFilter(field_name='component', label="RECEIVED", choices=component_list)
    date_from = DateFilter(field_name='date', lookup_expr='date__gte', label="DATE FROM", widget=DateInput(attrs={'type': 'date'}))
    date_to = DateFilter(field_name='date', lookup_expr='date__lte', label="DATE TO", widget=DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Employee_Record
        fields = ['employee_id',
                  'first_name',
                  'last_name', 
                  'department',
                  'client',
                  'component',
                  'date_from',
                  'date_to'
                  ]



