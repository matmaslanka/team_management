from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from .models import Employee, Task

# Create your views here.

class EmployeesView(ListView):
    template_name = 'team/employees_list.html'
    model = Employee
    context_object_name = 'employees'

class AddTaskView(CreateView):
    model = Task
    fields = '__all__'
    template_name = 'team/add_task.html'
    success_url = '/'


class TasksView(DetailView):
    template_name = 'team/tasks_list.html'
    model = Employee
    context_object_name = 'single_employee_task'


class SingleTaskView(DetailView):
    template_name = 'team/task_details.html'
    model = Task
    context_object_name = 'single_task'