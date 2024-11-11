from django.contrib import admin
from .models import Client, Department, Employee_Record, Component

admin.site.site_header = "HR Receiving Form System"

admin.site.register(Client)
admin.site.register(Department)
admin.site.register(Employee_Record)
admin.site.register(Component)

