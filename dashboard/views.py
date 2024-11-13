from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from receiving_app.models import Employee_Record
from django.http import HttpResponse
import datetime
from django.db.models import Q

from openpyxl.styles.borders import Border, Side, BORDER_THIN
from openpyxl import Workbook
from openpyxl.styles import *



def dashboard(request):

    # employee_record = Employee_Record.objects.all()

    # print('hello')

    # context = {
    #     'employee_record': employee_record
    # }

    return render(request, 'dashboard/dashboard.html')