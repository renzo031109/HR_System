from django.shortcuts import render, redirect
from .models import Staff_Record, Client, Department
from .forms import ReceivedModelFormSet



# Create your views here.
def summary_released(request):
    records = Staff_Record.objects.all()
    context = {'records': records}
    return render(request, 'receiving_app/summary_report.html', context)


def add_record(request):
    if request.method == 'POST':
        formset = ReceivedModelFormSet(request.POST)
        #check the validity of form
        if formset.is_valid():
            for form in formset:
                #check if employee id is not null
                if form.cleaned_data.get('employee_id'):

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

                    return redirect('submitted')

    else:
        formset = ReceivedModelFormSet(queryset=Staff_Record.objects.none())

    context = {'formset': formset}
    return render(request, 'receiving_app/add_record.html', context)


def submitted(request):
    return render(request, 'receiving_app/submitted.html')
 