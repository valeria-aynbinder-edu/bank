from django.urls import path

from . import views

# Creating URLConf
urlpatterns = [
    path('', views.index, name='index'),
    path('branches', views.branches, name='branches'),
    path('branches/<int:branch_id>', views.branch_details, name='branch_details'),
    path('branches/add', views.add_branch, name='add_branch'),

    path('employees', views.employees, name='employees'),
    path('employees/<int:employee_id>', views.employee_details, name='employee_details'),


    path('bank_accounts', views.accounts, name='bank_accounts'),
    path('bank_accounts/<int:account_id>', views.account_details, name='bank_account_details'),

    path('signup', views.signup, name='signup'),
    # path('login', views.login, name='login')
]