from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

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


class AddNewEmployeeView(CreateView):
    model = Employee
    fields = '__all__'
    template_name = 'team/add_new_employee.html'
    success_url = '/'


class UpdateEmployeeView(UpdateView):
    model = Employee
    fields = ['employee_task']
    template_name = 'team/add_task_to_employee.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        employee_id = self.kwargs.get('pk')
        context['employee_id'] = employee_id
        return context


class AddTaskToEmployeeView(CreateView):
    model = Task
    fields = '__all__'
    template_name = 'team/add_task_to_employee.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        employee_id = self.kwargs.get('id')
        context['employee_id'] = employee_id
        return context

    def form_valid(self, form):
        employee = Employee.objects.get(pk=self.kwargs['pk'])
        task = form.save()
        employee.employee_task.add(task)
        return super().form_valid(form)

    success_url = '/'


class UpdateTaskView(UpdateView):
    model = Task
    fields = '__all__'
    template_name = 'team/task_update.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task_id = self.kwargs.get('pk')
        context['task_id'] = task_id
        return context


class TasksView(DetailView):
    template_name = 'team/tasks_list.html'
    model = Employee
    context_object_name = 'single_employee_task'


class SingleTaskView(DetailView):
    template_name = 'team/task_details.html'
    model = Task
    context_object_name = 'single_task'
