# -*- coding: utf-8 -*-

from django import forms

from wzw.models import Expense, Person, Group


# Formularvorlage für Gruppenbeschreibung und Gruppenname
class GroupForm(forms.Form):
    name = forms.CharField(max_length=32)
    description = forms.CharField(max_length=128)


# Formular zum ändern des Gruppennamen und der Gruppenbeschreibung
# Hierbei wird die alte Beschreibung, soweit vorhanden, mit übergeben
class ChangeGroup(forms.ModelForm):
    class Meta:
        model = Group
        exclude = ()


# Anzeige des Eingabefeldes auf der Startseite für das Anzeigen einer Gruppe
class OpenGroupForm(forms.Form):
    group_token = forms.CharField(label='Token', max_length=19, required=True)


# Formular zum Erstellen einer Ausgabe
class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        widgets = {'group': forms.HiddenInput()}
        exclude = {'createDate'}

    # Function to set scope for expense
    def set_person_scope(self, grouptoken):
        person = Person.objects.filter(group=grouptoken)
        self.fields['costPersons'].queryset = person
        self.fields['owner'].queryset = person


# Formular zum Anlegen einer Person
class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        widgets = {'group': forms.HiddenInput()}
        exclude = ()
