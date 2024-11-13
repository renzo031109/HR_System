from django.contrib import admin
from .models import Client, Department, Employee_Record, Component, Statistics

admin.site.site_header = "HR Receiving Form System"

admin.site.register(Client)
admin.site.register(Department)
admin.site.register(Employee_Record)
admin.site.register(Component)
admin.site.register(Statistics)

