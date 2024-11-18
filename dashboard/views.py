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



# def dashboard(request):
#     # Get the current date, month, and year
#     now = datetime.datetime.now()
#     current_year = now.year
#     current_month = now.month
#     today = now.date()

#     # Calculate today's transactions
#     transaction_today = Statistics.objects.filter(date__date=today).count()

#     # Calculate monthly transactions
#     transaction_month = Statistics.objects.filter(date__year=current_year, date__month=current_month).count()

#     # Get the list of monthly records 
#     monthly_records = Statistics.objects.filter(date__year=current_year, date__month=current_month)

#     # Group components and count released items for today
#     component_stat = (Employee_Record.objects
#                       .filter(date__date=today)
#                       .values('component__component')
#                       .annotate(total_count=Sum('count'))
#                       .order_by('-total_count'))

    
#     component_sta_month = (Employee_Record.objects
#                       .filter(date__date=monthly_records)
#                       .values('component__component')
#                       .annotate(total_count=Sum('count'))
#                       .order_by('-total_count'))




#     context = {
#         'transaction_month': transaction_month,
#         'transaction_today': transaction_today,
#         'component_stat': component_stat,
#         'component_sta_month': component_sta_month
#     }

#     return render(request, 'dashboard/dashboard.html', context)



def dashboard(request):
    # Get the current date, month, and year
    now = datetime.datetime.now()
    current_year = now.year
    current_month = now.month
    today = now.date()

    # Calculate today's transactions
    transaction_today = Statistics.objects.filter(date__date=today).count()

    # Calculate monthly transactions
    transaction_month = Statistics.objects.filter(date__year=current_year, date__month=current_month).count()

    # Get the list of monthly records
    monthly_records = Statistics.objects.filter(date__year=current_year, date__month=current_month)

    # Group components and count released items for today
    component_stat = (Employee_Record.objects
                      .filter(date__date=today)
                      .values('component__component')
                      .annotate(total_count=Sum('count'))
                      .order_by('-total_count'))

    # Group components and count released items for the current month
    component_stat_month = (Employee_Record.objects
                            .filter(date__year=current_year, date__month=current_month)
                            .values('component__component')
                            .annotate(total_count=Sum('count'))
                            .order_by('-total_count'))

    context = {
        'transaction_month': transaction_month,
        'transaction_today': transaction_today,
        'component_stat': component_stat,
        'component_stat_month': component_stat_month
    }

    return render(request, 'dashboard/dashboard.html', context)




