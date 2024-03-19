from django.shortcuts import render
from django.views.generic import ListView

from .models import Team

# Create your views here.

class EmployeesView(ListView):
    template_name = 'team/employees_list.html'
    model = Team