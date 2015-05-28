from django import forms

from wzw.models import Expense, Person, Group


class GroupForm(forms.Form):
    name = forms.CharField(max_length=32)
    description = forms.CharField(max_length=128)


class ChangeGroup(forms.ModelForm):
    class Meta:
        model = Group
        exclude = ()


class OpenGroupForm(forms.Form):
    group_token = forms.CharField(label='Token', max_length=19, required=True)


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        widgets = {'group': forms.HiddenInput()}
        exclude = {'createDate'}


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        widgets = {'group': forms.HiddenInput()}
        exclude = ()
