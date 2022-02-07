from django.conf import settings
from django.db import transaction, IntegrityError
from django.http import HttpResponseNotFound, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_http_methods

from .forms import BranchForm, EmployeeForm, AccountForm
from .models import Branch, BranchEmployee, Employee, Account
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    # if not request.user.is_authenticated:
    #     return HttpResponse("You are not logged in")
        # return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    return render(request, "index.html")

@login_required
def branches(request):
    # branches = Branch.objects.filter(is_deleted=False).select_related("city")
    branches = Branch.objects.filter(is_deleted=False).prefetch_related("city")
    return render(request, "branches.html", context={'branches': branches})

@login_required
def branch_details(request, branch_id):
    # branch = get_object_or_404(Branch, pk=branch_id)

    branch = Branch.objects.get(is_deleted=False, pk=branch_id)


    if request.method == 'GET':
        form = BranchForm(instance=branch)
    elif request.method == 'POST':
        form = BranchForm(instance=branch, data=request.POST)
        if form.is_valid():
            form.save()
    elif request.method == 'DELETE':
        branch.is_deleted = True
        branch.save()
        return HttpResponse()

    return render(request, "branch_details.html",
                  context={'form': form, 'branch_id': branch.id})

@login_required
def employees(request):
    all_employees = Employee.objects.all()
    return render(request, "employees.html", context={'employees': all_employees})


@require_http_methods(["GET", "POST"])
@login_required
def employee_details(request, employee_id):

    employee = get_object_or_404(Employee, id=employee_id)
    edit_mode = False

    if request.method == 'GET':
        edit_mode = request.GET.get('mode', '').lower() == 'edit'
        form = None
        if edit_mode:
            form = EmployeeForm(instance=employee)

    else:
        form = EmployeeForm(instance=employee, data=request.POST)
        if form.is_valid():
            form.save(commit=True)


    return render(request, "employee_details.html",
                  context={'employee': employee,
                           'is_edit_mode': edit_mode,
                           'form': form})

@login_required
def add_branch(request):
    if request.method == 'GET':
        form = BranchForm()
        return render(request, "add_branch.html", context={'form': form})
    elif request.method == 'POST':
        # city = request.POST['city']
        # address = request.POST['address']
        # branch = Branch(city=city, address=address)
        # branch.save()
        # return branches(request)

        form = BranchForm(data=request.POST)
        if form.is_valid():
            # city = form.cleaned_data['city']
            # address = form.cleaned_data['address']
            # branch = Branch(city=city, address=address)
            # branch.save()
            form.save()
            return branches(request)
        else:
            return render(request, "add_branch.html", context={'form': form})


# def show_transaction():
#     try:
#         with transaction.atomic():
#             #begin
#             b = Branch(city='yy',address='dfgdf')
#             be = BranchEmployee(branch=b, employee=emp)
#             #commit
#     except IntegrityError:
#         pass

@login_required
def accounts(request):
    all_accounts = Account.objects.filter(is_deleted=False) #consider adding to some common place
    return render(request, "accounts.html",
                  context={'accounts': all_accounts})

@login_required
@require_http_methods(["GET", "POST"])
def account_details(request, account_id):
    account = get_object_or_404(Account, id=account_id)

    if request.method == 'GET':
        form = AccountForm(instance=account)
        return render(request=request, template_name='account_details.html', context={'form': form, 'account': account})
    else:
        form = AccountForm(instance=account, data=request.POST)
        if form.is_valid():
            form.save()
        return render(request=request, template_name='account_details.html', context={'form': form, 'account': account})


from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})