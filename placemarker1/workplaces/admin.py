# workplaces/admin.py
from django.contrib import admin
from .models import Workplace

class WorkplaceAdmin(admin.ModelAdmin):
    list_display = ('number', 'get_type_display', 'status', 'department')
    list_filter = ('status', 'type')
    search_fields = ('number', 'department')
    ordering = ('number',)

    def get_type_display(self, obj):
        return obj.get_type_display()
    get_type_display.short_description = 'Тип'

# Убедитесь, что регистрация происходит только один раз
try:
    admin.site.register(Workplace, WorkplaceAdmin)
except admin.sites.AlreadyRegistered:
    pass
