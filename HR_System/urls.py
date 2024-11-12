"""
URL configuration for HR_System project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from receiving_app import views as received_views
from django.contrib.auth import views as auth_views
from user import views as user_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', received_views.summary_released, name='summary_received'),
    path('add_record/', received_views.add_record, name='add_record'),
    path('submitted/', received_views.submitted, name='submitted'),
    path('dashboard', received_views.dashboard, name='dashboard'),
    path('delete_employee/<str:id>/', received_views.delete_employee, name = 'delete_employee'),
    path('export_excel_record/', received_views.export_excel_record, name='export_excel_record'),

    path('register/', user_view.register, name='user-register'),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='user-login'),
    path('logout/', user_view.logoutPage, name = 'user-logout'),
]
