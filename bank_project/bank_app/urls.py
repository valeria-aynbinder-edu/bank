from django.urls import path

from . import views

# Creating URLConf
urlpatterns = [
    path('', views.index, name='index'),
    path('branches', views.branches, name='branches'),
    path('branches/<int:branch_id>', views.branch_details, name='branch_details'),
    path('employees', views.employees, name='employees'),
    path('employees/<int:employee_id>', views.employee_details, name='employee_details'),
]