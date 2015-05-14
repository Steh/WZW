from django.http import HttpResponse
from django.views.generic import View
from django.template import loader


class Index(View):

    # Ergebnis bei GET
    def get(self, request):

        t = loader.get_template('wzw/index.html')
        return HttpResponse(t.render())

    # Ergebnis bei POST
    def post(self, request):

        return HttpResponse('result post')