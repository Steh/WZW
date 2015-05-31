from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages

from wzw.forms import GroupForm, OpenGroupForm, ExpenseForm, PersonForm, ChangeGroup
from wzw.models import Group, Person, Expense


class Index(View):
    @staticmethod
    def get(request):

        form_new_group = GroupForm()
        form_open_group = OpenGroupForm()
        return render(request, 'Wzw/index.html', {'form_new_group': form_new_group, 'form_open_group': form_open_group})

    @staticmethod
    def post(request):
        if 'new_group' in request.POST:
            group = Group.objects.create()
            return HttpResponseRedirect('group/' + group.token + '/group/new')

        if 'open_group' in request.POST:
            form = OpenGroupForm(request.POST)

            if form.is_valid():
                token = form.cleaned_data['group_token']
                return HttpResponseRedirect('/group/' + token)

        # TODO richtig machen
        return HttpResponseRedirect('/')


class GroupIndex(View):
    @staticmethod
    def get(request, token):
        group = get_object_or_404(Group, token=token)
        group.save()

        expense = Expense.objects.filter(group=group)
        person = Person.objects.filter(group=group)

        form_change_group = ChangeGroup(initial={'name': group.name}, )

        form_new_expense = ExpenseForm(initial={'group': group.id}, )
        form_new_expense.fields['costPersons'].queryset = person
        form_new_expense.fields['owner'].queryset = person

        return render(request, 'Wzw/group.html',
                      {'form_new_expense': form_new_expense,
                       'form_change_group': form_change_group,
                       'expense': expense,
                       'group': group,
                       'person': person})


class GroupView(View):
    @staticmethod
    def get(request, token):
        group = get_object_or_404(Group, token=token)
        group.save()

        form = ChangeGroup()
        context = {'form': form, 'group': group}
        return render(request, 'wzw/group.html', context)

    @staticmethod
    def post(request, token):
        group = get_object_or_404(Group, token=token)
        group.save()

        if 'change_group' in request.POST:
            form = ChangeGroup(instance=group, data=request.POST)

            if form.is_valid():
                form.save()

            else:
                message = 'Eingabe war nicht gueltig'
                context = {'form': form, 'message': message, 'group': group}
                return render(request, 'wzw/editGroup.html', context)

        if 'delete_group' in request.POST:
            group.delete()
            return HttpResponse('Gruppe wurde geloescht ' + token)


# TODO bisschen unglueglich gewaehlt, da man so die new group url immer aufrufen kann :)
class NewGroupView(View):
    @staticmethod
    def get(request, token):
        group = get_object_or_404(Group, token=token)
        group.save()

        form = ChangeGroup(instance=group)
        context = {'group': group, 'form': form}
        return render(request, 'wzw/newGroup.html', context)

    # TODO schauen, warum hier nicht der Gruppenname und die Beschreibung uebergeben werden
    @staticmethod
    def post(request, token):
        group = get_object_or_404(Group, token=token)
        group.save()

        if 'edit_group' in request.POST:
            form = ChangeGroup(instance=group, data=request.POST)

            if form.is_valid():
                form.save()
                messages.info(request, 'Gruppe wurde erstellt')

            else:
                messages.warning(request, 'Gruppe KONNTE NICHT erstellt werden')

        return HttpResponseRedirect('/group/' + group.token)


class EditGroupView(View):
    @staticmethod
    def get(request, token):
        group = get_object_or_404(Group, token=token)
        group.save()

        form = ChangeGroup(instance=group)
        context = {'group': group, 'form': form}
        return render(request, 'wzw/editGroup.html', context)

    @staticmethod
    def post(request, token):
        group = get_object_or_404(Group, token=token)
        group.save()

        if 'edit_group' in request.POST:
            form = ChangeGroup(instance=group, data=request.POST)

            if form.is_valid():
                form.save()
                messages.info(request, 'Gruppe wurde angepasst')

            else:
                messages.warning(request, 'Gruppe KONNTE NICHT angepasst werden')

        return HttpResponseRedirect('/group/' + group.token + '/group/')


class DeleteGroupView(View):
    @staticmethod
    def get(request, token):
        group = get_object_or_404(Group, token=token)
        group.save()

        context = {'group': group}
        return render(request, 'wzw/deleteGroup.html', context)

    @staticmethod
    def post(request, token):
        group = get_object_or_404(Group, token=token)
        group.save()

        if 'apply_delete_group' in request.POST:
            group.delete()
            messages.info(request, 'Gruppe wurde erfolgreich geloescht')
            return HttpResponseRedirect('/')

        messages.warning(request, 'Es wurde keine Gruppe uebergeben')
        return HttpResponseRedirect('/group/' + group.token + '/group/')


class PersonView(View):
    @staticmethod
    def get(request, token):
        group = get_object_or_404(Group, token=token)
        group.save()

        person = Person.objects.filter(group=group)

        context = {'person': person, 'group': group}
        return render(request, 'wzw/person.html', context)

    @staticmethod
    def post(request, token):
        group = get_object_or_404(Group, token=token)
        group.save()

        messages.warning(request, 'POST hier nicht zulaessig')
        return HttpResponseRedirect('/group/' + group.token + '/person/')


class NewPersonView(View):
    @staticmethod
    def get(request, token):
        group = get_object_or_404(Group, token=token)
        group.save()

        person = Person.objects.filter(group=group)
        form = PersonForm(initial={'group': group.id})

        context = {'form': form, 'person': person, 'group': group}
        return render(request, 'wzw/newPerson.html', context)

    @staticmethod
    def post(request, token):
        group = get_object_or_404(Group, token=token)
        group.save()

        form = PersonForm(request.POST)

        if form.is_valid():
            form.save()
            messages.info(request, 'Person wurde angelegt')
        else:
            messages.warning(request, 'Person konnte nicht angelegt werden')

        return HttpResponseRedirect('/group/' + group.token + '/person/')


class EditPersonView(View):
    @staticmethod
    def get(request, token):
        group = get_object_or_404(Group, token=token)
        group.save()

        messages.info(request, 'Es wurde keine Person uebergeben')
        return HttpResponseRedirect('/group/' + group.token + '/person/')

    @staticmethod
    def post(request, token):
        group = get_object_or_404(Group, token=token)
        group.save()

        person_id = request.POST['person_id']
        person = get_object_or_404(Person, id=person_id)

        personReport = person.personcostreport()

        if 'change_person' in request.POST:

            form = PersonForm(instance=person)
            context = {'form': form,
                       'group': group,
                       'person': person,
                       'report': personReport}

            return render(request, 'wzw/editPerson.html', context)

        elif 'apply_change_person' in request.POST:

            form = PersonForm(instance=person, data=request.POST)

            if form.is_valid():
                form.save()

                messages.info(request, 'Person wurde angepasst')
                return HttpResponseRedirect('/group/' + group.token + '/person/')
            else:
                messages.warning(request, 'Aenderungen konnten nicht durchgefuehrt werden')
                return HttpResponseRedirect('/group/' + group.token + '/person/')

        # default
        else:
            group = get_object_or_404(Group, token=token)
            group.save()

            messages.info(request, 'Es wurde keine Person uebergeben')
            return HttpResponseRedirect('/group/' + group.token + '/person/')


class DeletePersonView(View):
    @staticmethod
    def get(request, token):
        group = get_object_or_404(Group, token=token)
        group.save()

        messages.info(request, 'Es wurde keine Person uebergeben')
        return HttpResponseRedirect('/group/' + group.token + '/person/')

    @staticmethod
    def post(request, token):
        group = get_object_or_404(Group, token=token)
        group.save()

        person_id = request.POST['person_id']
        person = get_object_or_404(Person, id=person_id)

        if 'delete_person' in request.POST:
            expenseowner = Expense.objects.filter(owner=person)
            expensecostperson = Expense.objects.filter(costPersons=person)

            context = {'person': person,
                       'group': group,
                       'expenseowner': expenseowner,
                       'expensecostperson': expensecostperson}
            return render(request, 'wzw/deletePerson.html', context)

        elif 'apply_delete_person' in request.POST:
            personid = person.id
            personname = person.name
            person.delete()

            if (Person.objects.filter(id=personid)).count() == 0:
                messages.info(request, personname + ' wurde geloescht')
                return HttpResponseRedirect('/group/' + group.token + '/person/')
            else:
                messages.warning(request, 'Person konnte nicht geloescht werden')
                return HttpResponseRedirect('/group/' + group.token + '/person/')

        # default
        else:
            group = get_object_or_404(Group, token=token)
            group.save()

            messages.info(request, 'Es wurde keine Person uebergeben')
            return HttpResponseRedirect('/group/' + group.token + '/person/')


class ExpenseView(View):
    @staticmethod
    def get(request, token):
        group = get_object_or_404(Group, token=token)
        group.save()

        expense = Expense.objects.filter(group=group)
        person = Person.objects.filter(group=group)

        form_new_expense = ExpenseForm(initial={'group': group.id}, )
        form_new_expense.fields['costPersons'].queryset = person
        form_new_expense.fields['owner'].queryset = person

        return render(request, 'Wzw/expense.html',
                      {'form': form_new_expense,
                       'expense': expense,
                       'group': group,
                       'person': person})

    @staticmethod
    def post(request, token):
        group = get_object_or_404(Group, token=token)
        group.save()

        if 'new_expense' in request.POST:
            form = ExpenseForm(request.POST)

            if form.is_valid():
                form.save()

        if 'edit_expense' in request.POST:
            data = request.POST['expense_id']

            expense = get_object_or_404(Expense, id=data)
            expenses = Expense.objects.filter(group=group)
            person = Person.objects.filter(group=group)

            form = ExpenseForm(instance=expense)
            form.fields['costPersons'].queryset = person
            form.fields['owner'].queryset = person

            context = {'form_change_expense': form, 'expense': expenses, 'group': group, 'person': person}

            return render(request, 'Wzw/expense.html', context)

        return HttpResponseRedirect('/group/' + token + '/expense/')


class NewExpenseView(View):
    @staticmethod
    def get(request, token):
        group = get_object_or_404(Group, token=token)
        group.save()

        person = Person.objects.filter(group=group)

        form = ExpenseForm(initial={'group': group.id}, )
        form.fields['costPersons'].queryset = person
        form.fields['owner'].queryset = person

        context = {'form': form, 'group': group, 'person': person}
        return render(request, 'Wzw/newExpense.html', context)

    @staticmethod
    def post(request, token):
        group = get_object_or_404(Group, token=token)
        group.save()

        if 'new_expense' in request.POST:
            form = ExpenseForm(request.POST)

            if form.is_valid():
                form.save()
                messages.info(request, 'Ausgabe wurde angelegt')
            else:
                # TODO Aktion bei Fehlerhafter eingabe
                messages.warning(request, 'Ausgabe konnte nicht angelegt werden')

            return HttpResponseRedirect('/group/' + token + '/expense/')


class EditExpenseView(View):
    # Bei GET   request: Auflistung aller Ausgaben
    #   Bei POST  request: wenn gueltige ID uebergeben wurde, kann die Ausgabe bearbeitet werden, sonst 404
    @staticmethod
    def get(request, token):
        group = get_object_or_404(Group, token=token)
        group.save()

        messages.warning(request, 'Es wurde keine Ausgabe gefunden')
        return HttpResponseRedirect('/group/' + token + '/expense/')

    @staticmethod
    def post(request, token):
        group = get_object_or_404(Group, token=token)
        group.save()

        # Wenn Formular auf der Seite ausgefuehrt wurde
        # TODO verbessern eingabe mehrere Personen
        if 'edit_expense' in request.POST:
            data = request.POST['expense_id']

            expense = get_object_or_404(Expense, id=data)
            person = Person.objects.filter(group=group)

            form = ExpenseForm(instance=expense)
            form.fields['costPersons'].queryset = person
            form.fields['owner'].queryset = person

            context = {'form': form, 'expense': expense, 'group': group, 'person': person}

            return render(request, 'Wzw/editExpense.html', context)

        elif 'apply_edit_expense' in request.POST:
            expenseid = request.POST['expense_id']
            form = ExpenseForm(request.POST)

            if form.is_valid():
                expense = get_object_or_404(Expense, id=expenseid)
                expense.name = form.cleaned_data['name']
                expense.description = form.cleaned_data['description']
                expense.debitDate = form.cleaned_data['debitDate']
                expense.cost = form.cleaned_data['cost']
                expense.owner = form.cleaned_data['owner']
                expense.costPersons = form.cleaned_data['costPersons']
                expense.save()

                # TODO MEssage bauen
                # messages.INFO(request, "Ausgabe wurde geaendert: " + expense.name)
                return HttpResponseRedirect('/group/' + group.token + '/expense')

            else:
                # TODO FORM EditExpenseView form not valid
                return
        else:
            messages.warning(request, 'Es wurde keine Ausgabe gefunden')

        # default return
        return HttpResponseRedirect('/group/' + token + '/expense/')


class DeleteExpenseView(View):
    @staticmethod
    def get(request, token):
        # Gruppen koennen nur per POST request geloescht werden
        # bei einem GET aufruf wird auf die expense seite umgeleitet und eine Nachricht ausgegeben
        group = get_object_or_404(Group, token=token)
        group.save()

        messages.warning(request, 'Es wurde keine Ausgabe gefunden')
        return HttpResponseRedirect('/group/' + token + '/expense/')

    @staticmethod
    def post(request, token):
        group = get_object_or_404(Group, token=token)
        group.save()

        data = request.POST.get('expense_id')
        expense = get_object_or_404(Expense, id=data)

        # bei Aufruf durch loeschen Button
        if 'delete_expense' in request.POST:
            context = {'expense': expense, 'group': group}
            return render(request, 'wzw/deleteExpense.html', context)

        # bei loeschbestaetigung
        if 'apply_delete_expense' in request.POST:
            messages.warning(request, "Ausgabe wurde erfolgreich geloescht: " + expense.name)
            expense.delete()

            return HttpResponseRedirect('/group/' + token + '/expense/')

        messages.warning(request, 'Es wurde keine Ausgabe gefunden')
        return HttpResponseRedirect('/group/' + token + '/expense/')
