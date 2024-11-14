from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from receiving_app.models import Employee_Record, Statistics
from django.http import HttpResponse
import datetime
from django.db.models import Q
from django.db.models import Sum

from openpyxl.styles.borders import Border, Side, BORDER_THIN
from openpyxl import Workbook
from openpyxl.styles import *



def dashboard(request):

    stat = Statistics.objects.all()

    
                 
    # Get the current month and year
    now = datetime.datetime.now()
    current_year = now.year
    current_month = now.month

    today = datetime.datetime.now().date()

    #Transaction today summary
    transaction_today = 0
    for transaction_date in stat:
        if transaction_date.date.date() == datetime.datetime.now().date():
            transaction_today += 1


    # Filter for records in the current month
    stat = Statistics.objects.filter(date__year=current_year, date__month=current_month)
    transaction_month = stat.count()


    #This will group component and count released items today
    #componen__component will get the values of the field
    component_stat = (Employee_Record.objects
                      .filter(date__date=today)
                      .values('component__component')
                      .annotate(total_count=Sum('count'))
                      .order_by('-total_count')
                    )

    context = {

        'transaction_month': transaction_month,
        'transaction_today': transaction_today,
        'component_stat': component_stat
    }

    return render(request, 'dashboard/dashboard.html', context)