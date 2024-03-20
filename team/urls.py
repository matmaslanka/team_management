from django.urls import path
from . import views

urlpatterns = [
    path('', views.EmployeesView.as_view(), name='index'),
    path('tasks/add', views.AddTaskView.as_view(), name='add_task'),
    path('employees/<int:pk>', views.TasksView.as_view(), name='employee_id'),
    path('tasks/<int:pk>', views.SingleTaskView.as_view(), name='task_id')

]
