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

    # Filtert die moeglichen Person
    def __init__(self, persons_group, *args, **kwargs):
        super(newExpenseForm, self).__init__(*args, **kwargs)
        self.fields['costPersons'].queryset = Person.objects.filter(group=persons_group)
        self.fields['owner'].queryset = Person.objects.filter(group=persons_group)

    class Meta:
        model = Expense
        widgets = {'group': forms.HiddenInput()}
        exclude = ()

class newPersonForm(forms.ModelForm):
    class Meta:
        model = Person
        widgets = {'group': forms.HiddenInput()}
        exclude = ()