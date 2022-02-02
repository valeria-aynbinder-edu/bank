from django.db import transaction, IntegrityError
from django.http import HttpResponseNotFound, HttpResponse
from django.shortcuts import render, get_object_or_404

from .forms import BranchForm
from .models import Branch, BranchEmployee


def index(request):
    return render(request, "index.html")


def branches(request):
    branches = Branch.objects.filter(is_deleted=False)
    return render(request, "branches.html", context={'branches': branches})


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

def employees(request):
    return render(request, "employees.html")


def employee_details(request, employee_id):
    return None


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

