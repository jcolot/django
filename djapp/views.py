from django.views.generic import CreateView
from django.http import HttpResponse
from .models import Registrar
import requests


class RegistrationView(CreateView):
    model = Registrar
    fields = ['name', 'country', 'city', 'language', 't_and_c']

    def form_valid(self, form):
        self.object = form.save()
        url = 'http://www.mocky.io/v2/5db6b5f42f000058007fe988'
        payload = {'name': 'test'}
        headers = {'authentication-token': 'my-token'}
        r = requests.post(url, data = payload, headers = headers)
        return HttpResponse(r)

