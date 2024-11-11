from django.shortcuts import render, redirect
from .models import Staff_Record, Client, Department, Component
from .forms import ReceivedModelFormSet



# Create your views here.
def summary_released(request):
    records = Staff_Record.objects.all()
    context = {'records': records}
    return render(request, 'receiving_app/summary_report.html', context)


def add_record(request):

    # create a list to hold the first value input in the formset
    employee_id_list = []
    first_name_list = []
    last_name_list = []

    if request.method == 'POST':
        formset = ReceivedModelFormSet(request.POST)
        #check the validity of form
        if formset.is_valid():
            for form in formset:

                #check if employee id is not null
                if form.cleaned_data.get('component'):
                    #assign input value to variables
                    add_client = form.cleaned_data.get('client')
                    add_department = form.cleaned_data.get('department')
                    add_employee_id = form.cleaned_data.get('employee_id')
                    add_first_name = form.cleaned_data.get('first_name')
                    add_last_name = form.cleaned_data.get('last_name')


                    try:
                        #assign value to foreign keys
                        client = Client.objects.get(client=add_client)
                        department = Department.objects.get(department=add_department)
                    except:
                        pass

                    #hold the first value to a list
                    employee_id_list.append(add_employee_id)
                    first_name_list.append(add_first_name)
                    last_name_list.append(add_last_name)


                    received_formset = form.save(commit=False)
                    received_formset.client = client
                    received_formset.department = department
                    received_formset.employee_id = employee_id_list[0]
                    received_formset.first_name = first_name_list[0]
                    received_formset.last_name = last_name_list[0]
                    received_formset.save()
    
            return redirect('submitted')

    else:
        formset = ReceivedModelFormSet(queryset=Staff_Record.objects.none())

    context = {'formset': formset}
    return render(request, 'receiving_app/add_record.html', context)


def submitted(request):
    return render(request, 'receiving_app/submitted.html')


def dashboard(request):
    return render(request, 'receiving_app/dashboard.html')
 

def delete_employee(request, id):
    print(id)
    if request.method == 'POST':
        employee = Staff_Record.objects.get(id=id)

        employee.delete()
    return redirect('summary_received')