from django.urls import path
from . import views

urlpatterns = [
    path('', views.EmployeesView.as_view(), name='index'),
    path('tasks/add', views.AddTaskView.as_view(), name='add_task'),
    path('employees/add_new_employee',
         views.AddNewEmployeeView.as_view(), name='add_new_employee'),
    path('employees/<int:pk>/add-task/',
         views.AddTaskToEmployeeView.as_view(), name='add_task_to_employee'),
    path('employees/<int:pk>/update/',
         views.UpdateEmployeeView.as_view(), name='update_employee'),
    path('employees/<int:pk>', views.TasksView.as_view(), name='employee_id'),
    path('tasks/<int:pk>', views.SingleTaskView.as_view(), name='task_id'),
    path('tasks/<int:pk>/update/', views.UpdateTaskView.as_view(), name='update_task')
]
