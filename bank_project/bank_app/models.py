from django.db import models


class BankModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True


class City(models.Model):
    name = models.CharField(null=False, blank=False, max_length=128)

    def __str__(self):
        return f"{self.name}"


# Create your models here.
class Branch(BankModel):

    # city = models.CharField(null=False, blank=False, max_length=128)
    city = models.ForeignKey(City, on_delete=models.RESTRICT, null=True, blank=True)
    address = models.CharField(null=False, blank=False, max_length=512)

    class Meta:
        db_table = "branches"

    def __str__(self):
        return f"{self.city} {self.address}"


class Employee(BankModel):

    passport_num = models.CharField(null=False, blank=False, max_length=128, unique=True)
    first_name = models.CharField(null=False, blank=False, max_length=128)
    last_name = models.CharField(null=False, blank=False, max_length=128)
    birth_date = models.DateField(null=True, blank=True)
    city = models.CharField(null=False, blank=False, max_length=128)
    address = models.CharField(null=False, blank=False, max_length=512)

    class Meta:
        db_table = "employees"


class BranchEmployee(BankModel):

    employee = models.ForeignKey(Employee, models.RESTRICT)
    branch = models.ForeignKey(Branch, models.RESTRICT)
    position = models.CharField(null=False, blank=False, max_length=128)

    class Meta:
        db_table = "branch_employees"