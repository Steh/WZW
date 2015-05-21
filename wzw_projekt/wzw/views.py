from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render
from django.http import HttpResponseRedirect

from wzw.forms import newGroupForm, openGroupForm
from wzw.models import Group


class Index(View):
    # Ergebnis bei GET
    @staticmethod
    def get(request):

        form_create = newGroupForm()
        form_open = openGroupForm()
        return render(request, 'Wzw/index.html', {'form_create': form_create, 'form_open': form_open})

    # Ergebnis bei POST
    @staticmethod
    def post(request):
        if 'new_group' in request.POST:
            form = newGroupForm(request.POST)

            if form.is_valid():
                name = form.cleaned_data['new_group_name']
                group = Group.objects.create(name=name)

                return HttpResponseRedirect('/group/' + group.token)
            else:
                return HttpResponse('Gruppe konnte nicht angelegt werden')

        if 'open_group' in request.POST:
            form = openGroupForm(request.POST)

            if form.is_valid():
                token = form.cleaned_data['group_token']
                return HttpResponseRedirect('/group/' + token)

        return HttpResponse('geht nicht')


class GroupDetail(View):
    @staticmethod
    def get(request, token):
        # aufrufen der Gruppe
        try:
            group = Group.objects.get(token=token)
        except:
            return HttpResponse('Gruppe nicht vorhanden (' + token + ')')

        # aktualisiert lastLogon
        group.save()

        return HttpResponse(group)

    ''' Ergebnis bei POST '''

    @staticmethod
    def post(request):

        return HttpResponse('result post')
