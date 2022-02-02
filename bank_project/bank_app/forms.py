from django import forms
from django.core.validators import RegexValidator
from django.forms import Select
from .models import Branch, City



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

