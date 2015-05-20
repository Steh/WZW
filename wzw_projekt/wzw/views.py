from django.http import HttpResponse
from django.views.generic import View
from django.template import loader
from wzw.models import Group

class Index(View):

    # Ergebnis bei GET
    def get(self, request):

        t = loader.get_template('wzw/index.html')
        return HttpResponse(t.render())

    # Ergebnis bei POST
    def post(self, request):

        return HttpResponse('result post')

class GroupDetail(View):

    def get(self, request, token):
        # aufrufen der Gruppe
        try:
            group = Group.objects.get(token=token)
        except:
            return HttpResponse('Gruppe nicht vorhanden (' + token + ')')

        # aktualisiert lastLogon
        group.save()

        return HttpResponse(group)

    ''' Ergebnis bei POST '''
    def post(self, request):

        return HttpResponse('result post')
