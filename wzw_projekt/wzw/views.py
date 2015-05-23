^from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

from wzw.forms import newGroupForm, openGroupForm, newExpenseForm, newPersonForm, changeGroupName
from wzw.models import Group, Person, Expense


class Index(View):
    # Ergebnis bei GET
    @staticmethod
    def get(request):

        form_new_group = newGroupForm()
        form_open_group = openGroupForm()
        return render(request, 'Wzw/index.html', {'form_new_group': form_new_group, 'form_open_group': form_open_group})

    # Ergebnis bei POST
    @staticmethod
    def post(request):

        if 'new_group' in request.POST:
            form = newGroupForm(request.POST)

            if form.is_valid():
                group = form.save()

                return HttpResponseRedirect('/group/' + group.token)

        if 'open_group' in request.POST:
            form = openGroupForm(request.POST)

            if form.is_valid():
                token = form.cleaned_data['group_token']
                return HttpResponseRedirect('/group/' + token)

        return HttpResponse('geht nicht')


class GroupDetail(View):

    @staticmethod
    def get(request, token):

        # Aufrufen der Gruppe ueber den token
        group = get_object_or_404(Group, token=token)

        # aktualisiert lastLogon
        group.save()

        person = Person.objects.filter(group=group)
        expense = Expense.objects.filter(group=group)

        # Formulare erstellen
        form_change_group = changeGroupName(initial={'name': group.name}, )


        form_new_expense = newExpenseForm(initial={'group': group.id}, )
        form_new_expense.fields['costPersons'].queryset = person
        form_new_expense.fields['owner'].queryset = person

        form_new_person = newPersonForm(initial={'group': group.id}, )

        return render(request, 'Wzw/groupDetails.html', {'form_new_expense': form_new_expense, 'form_new_person': form_new_person, 'form_change_group': form_change_group, 'person': person, 'expense': expense})

    ''' Ergebnis bei POST '''

    @staticmethod
    def post(request, token):
        if 'new_person' in request.POST:
            form = newPersonForm(request.POST)

            if form.is_valid():
                form.save()

        if 'new_expense' in request.POST:
            form = newExpenseForm(request.POST)

            if form.is_valid():
                form.save()

        if 'change_group' in request.POST:
            group = get_object_or_404(Group, token=token)
            form = changeGroupName(instance=group, data=request.POST)

            if form.is_valid():
                form.save()

        if 'delete_group' in request.POST:
            group = get_object_or_404(Group, token=token)
            group.delete()
            return HttpResponse('Gruppe wurde geloescht ' + token)

        return HttpResponseRedirect('/group/' + token)
