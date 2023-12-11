from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
from solo.forms import BasicForm
import html


# Call as dumpdata('GET', request.GET)

def dumpdata(place, data):
    retval = ""
    if len(data) > 0:
        retval += '<p>Incoming ' + place + ' data:<br/>\n'
        for key, value in data.items():
            retval += html.escape(key) + '=' + html.escape(value) + '</br>\n'
        retval += '</p>\n'
    return retval


# Create your views here.
class SoloMain(LoginRequiredMixin, TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'solo/solo_app.html')

    def post(self, request):
        field1 = str(request.POST.get("field1")).strip()
        field2 = str(request.POST.get("field2")).strip()
        # the result concatenated, reversed, casefolded
        result = (field1 + field2)[::-1].casefold()
        print("This is a result!", result)
        return render(request, 'solo/solo_app.html', {'result' : result })
