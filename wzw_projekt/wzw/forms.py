from django import forms
from wzw.models import Expense, Person, Group


class newGroupForm(forms.ModelForm):
    class Meta:
        model = Group
        exclude = ()

class changeGroupName(forms.ModelForm):
    class Meta:
        model = Group
        exclude = ()

class openGroupForm(forms.Form):
    group_token = forms.CharField(label='Gruppen Token', max_length=19, required=True)

class newExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        widgets = {'group': forms.HiddenInput()}
        exclude = ()

class newPersonForm(forms.ModelForm):
    class Meta:
        model = Person
        widgets = {'group': forms.HiddenInput()}
        exclude = ()