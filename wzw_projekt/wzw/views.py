from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

from wzw.forms import NewGroupForm, OpenGroupForm, NewExpenseForm, NewPersonForm, ChangeGroup, DeletePersonForm
from wzw.models import Group, Person, Expense


class Index(View):
    # Ergebnis bei GET
    @staticmethod
    def get(request):

        form_new_group = NewGroupForm()
        form_open_group = OpenGroupForm()
        return render(request, 'Wzw/index.html', {'form_new_group': form_new_group, 'form_open_group': form_open_group})

    # Ergebnis bei POST
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

        return HttpResponse('geht nicht')


class GroupDetail(View):
    @staticmethod
    def get(request, token):

        # Aufrufen der Gruppe ueber den token
        group = get_object_or_404(Group, token=token)

        # aktualisiert lastLogon
        group.save()

        expense = Expense.objects.filter(group=group)

        # Formulare erstellen
        form_change_group = ChangeGroup(initial={'name': group.name}, )
        person = Person.objects.filter(group=group)

        form_new_expense = NewExpenseForm(initial={'group': group.id}, )
        form_new_expense.fields['costPersons'].queryset = person
        form_new_expense.fields['owner'].queryset = person



        return render(request, 'Wzw/detailsGroup.html',
                      {'form_new_expense': form_new_expense,
                       'form_change_group': form_change_group, 'expense': expense, 'group': group})

    ''' Ergebnis bei POST '''

    @staticmethod
    def post(request, token):
        if 'new_expense' in request.POST:
            form = NewExpenseForm(request.POST)

            if form.is_valid():
                form.save()

        return HttpResponseRedirect('/group/' + token)


class EditGroup(View):
    @staticmethod
    def get(request, token):
        group = get_object_or_404(Group, token=token)
        group.save()

        form = ChangeGroup()
        return render(request, 'wzw/editGroup.html', {'form': form})

    @staticmethod
    def post(request, token):
        if 'change_group' in request.POST:
            group = get_object_or_404(Group, token=token)
            form = ChangeGroup(instance=group, data=request.POST)

            if form.is_valid():
                form.save()

            else:
                message = 'Eingabe war nicht gueltig'
                return render(request, 'wzw/editGroup.html', {'form': form, 'message': message})

        if 'delete_group' in request.POST:
            group = get_object_or_404(Group, token=token)
            group.delete()
            return HttpResponse('Gruppe wurde geloescht ' + token)


class EditPerson(View):
    @staticmethod
    def get(request, token):
        group = get_object_or_404(Group, token=token)
        group.save()

        person = Person.objects.filter(group=group)

        form_new_person = NewPersonForm(initial={'group': group.id}, )
        form_delete_person = DeletePersonForm()

        context = {'form': form_new_person, 'form1': form_delete_person, 'person': person}
        return render(request, 'wzw/editPerson.html', context)

    @staticmethod
    def post(request, token):
        group = get_object_or_404(Group, token=token)
        group.save()

        if 'new_person' in request.POST:
            form = NewPersonForm(request.POST)

            if form.is_valid():
                form.save()

                person = Person.objects.filter(group=group)

                return render(request, 'wzw/editPerson.html', {'form': form, 'person': person})

            else:
                return HttpResponse('irgendwas geht schief')

        if 'delete_person' in request.POST:
            form = DeletePersonForm(request.POST)

            if form.is_valid():

                person = get_object_or_404(Person, id=form.id)
                return HttpResponse(person)
            else:
                return HttpResponse('neeee')


class EditExpense(View):
    @staticmethod
    def get(request, token):
        group = get_object_or_404(Group, token=token)
        group.save()

        form = ChangeGroup()
        return render(request, 'wzw/editGroup.html', {'form': form})