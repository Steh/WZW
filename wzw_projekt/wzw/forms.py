from django import forms


class newGroupForm(forms.Form):
    new_group_name = forms.CharField(label='Gruppen Name', max_length=32, required=False)

class openGroupForm(forms.Form):
    group_token = forms.CharField(label='Gruppen Token', max_length=19, required=True)