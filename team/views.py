from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Employee, Task

# Create your views here.

class EmployeesView(ListView):
    template_name = 'team/employees_list.html'
    model = Employee
    context_object_name = 'employees'


class TasksView(ListView):
    template_name = 'team/tasks_list.html'
    model = Task
    context_object_name = 'tasks'


class SingleTaskView(DetailView):
    template_name = 'team/task_details.html'
    model = Task
    context_object_name = 'single_task'