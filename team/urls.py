from django.urls import path
from . import views

urlpatterns = [
    path('', views.EmployeesView.as_view()),
    path('employees/tasks/<int:pk>', views.TasksView.as_view()),
    path('tasks/<int:pk>', views.SingleTaskView.as_view())
]