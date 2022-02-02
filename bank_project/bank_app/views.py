from django.shortcuts import render, get_object_or_404

from .models import Branch


def index(request):
    return render(request, "index.html")


def branches(request):
    branches = Branch.objects.all()
    return render(request, "branches.html", context={'branches': branches})


def branch_details(request, branch_id):
    branch = get_object_or_404(Branch, pk=branch_id)
    return render(request, "branch_details.html", context={'branch': branch})


def employees(request):
    return render(request, "employees.html")


def employee_details(request, employee_id):
    return None