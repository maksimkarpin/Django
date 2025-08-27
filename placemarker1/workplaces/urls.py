from django.urls import path
from. import views

urlpatterns = [
    path('', views.workplace_list, name='workplaces_list'),
    path('update/<int:pk>/', views.workplace_update, name='workplace_update'),
    path('delete/<int:pk>/', views.workplace_delete, name='workplace_delete'),
    path('occupied/', views.workplace_occupied, name='workplace_occupied'),
    path('create/', views.workplace_create, name='workplace_create'),
    path('add/', views.workplace_add, name='workplace_add'),
    path('edit/<int:pk>/', views.workplace_edit, name='workplace_edit'),
    path('add/', views.workplace_add, name='workplace_add'),

]
