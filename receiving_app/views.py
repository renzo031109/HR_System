from django.shortcuts import render
from .models import Staff_Record, Client, Department
from .forms import ReceivedFormSet



# Create your views here.
def summary_released(request):
    report = Staff_Record.objects.all()
    context = {'report': report}
    return render(request, 'receiving_app/summary_report.html', context)


def add_record(request):
    if request.method == 'POST':
        formset = ReceivedFormSet(request.POST)
        #check the validity of form
        if formset.is_valid():
            for form in formset:
                #check if employee id is not null
                if form.cleaned_data.get('employee_id'):
                    #get the value of the submitted form
                    # add_employee_id = form.cleaned_data.get('employee_id')
                    # add_last_name = form.cleaned_data.get('last_name')
                    # add_first_name = form.cleaned_data.get('first_name')
                    add_client = form.cleaned_data.get('client')
                    add_department = form.cleaned_data.get('department')

                    try:
                        client = Client.objects.get(client=add_client)
                        department = Department.objects.get(department=add_department)
                    except:
                        pass


                    received_formset = form.save(commit=False)
                    received_formset.client = client
                    received_formset.department = department
                    received_formset.save()

    else:
        formset = ReceivedFormSet()

    context = {'formset': formset}
    return render(request, 'receiving_app/add_record.html', context)
 