from django.contrib import admin
from .models import Client, Department, Staff_Record, Component

admin.site.site_header = "HR Receiving Form System"

admin.site.register(Client)
admin.site.register(Department)
admin.site.register(Staff_Record)
admin.site.register(Component)

