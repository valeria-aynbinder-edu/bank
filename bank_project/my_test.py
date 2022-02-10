# the following 4 lines setup and initialize Django app with your default app settings
# after calling these lines you can actually access DB using Django Models
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bank_project.settings")
import django
django.setup()

from bank_app.models import *

all_accounts = Account.objects.all()
print(f"Accounts: {all_accounts}")