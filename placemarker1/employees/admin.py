
from django.contrib import admin
from .models import Employee, Skill, EmployeeSkill

class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']

class EmployeeSkillAdmin(admin.ModelAdmin):
    list_display = ['employee', 'skill', 'level']
    list_filter = ['skill']

admin.site.register(Skill, SkillAdmin)
admin.site.register(EmployeeSkill, EmployeeSkillAdmin)