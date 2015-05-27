from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages

from wzw.forms import GroupForm, OpenGroupForm, ExpenseForm, NewPersonForm, ChangeGroup
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
            return HttpResponseRedirect('/group/' + group.token)

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


class PersonView(View):
    @staticmethod
    def get(request, token):
        group = get_object_or_404(Group, token=token)
        group.save()

        person = Person.objects.filter(group=group)

        form_new_person = NewPersonForm(initial={'group': group.id}, )

        context = {'form': form_new_person, 'person': person, 'group': group}
        return render(request, 'wzw/person.html', context)

    @staticmethod
    def post(request, token):
        group = get_object_or_404(Group, token=token)
        group.save()

        if 'new_person' in request.POST:
            form = NewPersonForm(request.POST)

            if form.is_valid():
                form.save()

                person = Person.objects.filter(group=group)

                context = {'form': form, 'person': person, 'group': group}
                return render(request, 'wzw/person.html', context)

            else:
                # TODO vernuenftige rueckgabe
                return HttpResponse('irgendwas geht schief')

        if 'delete_person' in request.POST:
            data = request.POST['person_id']
            person = get_object_or_404(Person, id=data)
            person.delete()

            return HttpResponseRedirect('/group/' + group.token + '/editPerson/')

        return HttpResponse('sollte nicht so sein')


class NewGroupView(View):
    @staticmethod
    def get(request, token):
        return

    @staticmethod
    def post(request, token):
        return


class EditGroupView(View):
    @staticmethod
    def get(request, token):
        group = get_object_or_404(Group, token=token)
        group.save()

        form = ChangeGroup(instance=group)
        context = {'group': group, 'form': form}
        return render(request, 'wzw\editGroup.html', context)

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


class NewPersonView(View):
    @staticmethod
    def get(request, token):
        return

    @staticmethod
    def post(request, token):
        return


class EditPersonView(View):
    @staticmethod
    def get(request, token):
        return

    @staticmethod
    def post(request, token):
        return


class DeletePersonView(View):
    @staticmethod
    def get(request, token):
        return

    @staticmethod
    def post(request, token):
        return


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
    #   Bei GET   request: Auflistung aller Ausgaben
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

        # bei aufruf durch loeschen Button
        if 'delete_expense' in request.POST:
            context = {'expense': expense, 'group': group}
            return render(request, 'wzw/deleteExpense.html', context)

        # bei loeschbestaetigung
        if 'apply_delete_expense' in request.POST:
            # TODO geht gerade nicht!!!
            messages.warning(request, "Ausgabe wurde erfolgreich geloescht: " + expense.name)
            expense.delete()

            return HttpResponseRedirect('/group/' + token + '/expense/')

        messages.warning(request, 'Es wurde keine Ausgabe gefunden')
        return HttpResponseRedirect('/group/' + token + '/expense/')