from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'position', 'department')
    search_fields = ('last_name', 'first_name', 'position')
    list_filter = ('department',)
