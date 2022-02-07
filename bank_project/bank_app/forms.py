from django import forms
from django.core.validators import RegexValidator
from django.db import transaction
from django.forms import Select, DateInput
from .models import Branch, City, Employee, BranchEmployee, Account


# class BranchForm(forms.Form):
    # city = forms.CharField(max_length=128, required=True,
    #                        validators=[RegexValidator("[A-Za-z]+", message="City can only contain letters")])
    # address = forms.CharField(max_length=512, required=True)


class BranchForm(forms.ModelForm):

    # city = forms.ChoiceField(choices=(('haifa', 'Haifa'), ('tel aviv', 'Tel Aviv')))
    city = forms.ModelChoiceField(queryset=City.objects.all(),
                                  widget=Select(attrs={'style': 'background-color:purple'}))

    class Meta:
        model = Branch
        # fields = ['address']
        fields = ['city', 'address']
    # fields = '__all__'


class MyDateWidget(DateInput):
    input_type = "date"




class EmployeeForm(forms.ModelForm):

    passport_num = forms.CharField(disabled=True)
    birth_date = forms.DateField(widget=MyDateWidget())
    position_details = forms.ModelMultipleChoiceField(
            queryset=BranchEmployee.objects.filter(is_deleted=False))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['position_details'].queryset = \
            BranchEmployee.objects.filter(is_deleted=False, employee_id=self.instance.id)

        self.fields["position_details"].initial = (
            self.fields['position_details'].queryset.values_list(
                'id', flat=True
            )
        )

    # def __init__(self, is_new_form, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     # self.fields['passport_num'].disabled = not is_new_form

    class Meta:
        model = Employee
        fields = '__all__'
        exclude = ['is_deleted']

    def save(self, commit=True):

        with transaction.atomic():
            # store employee
            self.instance.save()

            # branchEmployee
            qs = BranchEmployee.objects.filter(
                employee_id=self.instance.id, is_deleted=False)
            existing_ids = set([elem.id for elem in qs])
            new_ids_qs = self.cleaned_data['position_details']
            new_ids = set([elem.id for elem in new_ids_qs])
            ids_to_remove = existing_ids.difference(new_ids)
            # ids_to_add = new_ids.difference(existing_ids)
            set_deleted_qs = BranchEmployee.objects.filter(id__in=list(ids_to_remove))
            for elem in set_deleted_qs:
                elem.is_deleted = True
                elem.save()


# class EmployeeForm(forms.ModelForm):
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args,**kwargs) # populates the post
#         self.fields['position_details'].queryset = BranchEmployee.objects.filter(
#             employee_id=self.instance.id, is_deleted=False)
#         self.fields["position_details"].initial = (
#             self.fields['position_details'].queryset.values_list(
#                 'id', flat=True
#             )
#         )
#
#
#     # birth_date = forms.DateField(widget=forms.SelectDateWidget)
#     passport_num = forms.CharField(disabled=True)
#
#     position_details = forms.ModelMultipleChoiceField(
#         queryset=BranchEmployee.objects.filter(is_deleted=False))
#
#     def save(self, commit=True):
#         with transaction.atomic():
#             self.instance.save()
#             qs = BranchEmployee.objects.filter(employee_id=self.instance.id, is_deleted=False)
#             existing_ids = set([elem.id for elem in qs])
#             new_ids_qs = self.cleaned_data['position_details']
#             new_ids = set([elem.id for elem in new_ids_qs])
#             ids_to_remove = existing_ids.difference(new_ids)
#             ids_to_add = new_ids.difference(existing_ids)
#             set_deleted_qs = BranchEmployee.objects.filter(id__in=list(ids_to_remove))
#             for elem in set_deleted_qs:
#                 elem.is_deleted = True
#                 elem.save()
#         return self.instance
#
#     class Meta:
#         model = Employee
#         fields = '__all__'
#         exclude = ['is_deleted']
#
#         widgets = {
#             'birth_date': forms.DateInput(attrs={'type': 'date'})
#         }


class NewEmployeeForm(EmployeeForm):
    passport_num = forms.CharField(disabled=True)

class AccountForm(forms.ModelForm):

    class Meta:
        model = Account
        fields = '__all__'
