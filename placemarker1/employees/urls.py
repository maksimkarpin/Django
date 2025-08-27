# employees/urls.py
from django.urls import path, include
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.employee_list, name='employees_list'),
    path('create/', views.employee_create, name='employee_create'),
    path('update/<int:pk>/', views.employee_update, name='employee_update'),
    path('delete/<int:pk>/', views.employee_delete, name='employee_delete'),
    path('skills/add/', views.skill_create, name='skill_create'),
    path('admin/', admin.site.urls),
    path('employees/', views.employee_list, name='employee_list'),
    path('employees/create/', views.employee_create, name='employee_create'),
    path('skills/', views.skill_list, name='skill_list'),
    path('skills/add/', views.skill_add, name='skill_add'),
    path('skills/<int:pk>/edit/', views.skill_edit, name='skill_edit'),
    path('skills/<int:pk>/delete/', views.skill_delete, name='skill_delete'),
]
