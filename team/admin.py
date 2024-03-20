from django.contrib import admin

from .models import Employee, Task

# Register your models here.


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('user_first_name', 'user_last_name', 'position',)
    # prepopulated_fields = {'slug':('user_last_name',)}


class TaskAdmin(admin.ModelAdmin):
    list_display = ('task_title', 'task_status',)


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Task, TaskAdmin)
