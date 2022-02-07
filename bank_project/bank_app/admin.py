from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Branch)
admin.site.register(Employee)
admin.site.register(BranchEmployee)
admin.site.register(Customer)
admin.site.register(Account)
admin.site.register(AccountOwner)

