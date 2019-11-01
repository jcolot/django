from django import forms
from djapp.models import Language, Registrar
from django.shortcuts import get_object_or_404, render


class RegistrarForm(forms.ModelForm):
    class Meta:
        model = Registrar
        fields = ['name', 'country', 'city', 'language']

#class RegistrarForm(forms.Form):
#    name = forms.CharField(max_length=32, label='Name')
#    country = forms.ChoiceField(required=True,label='Country')
#    city = forms.CharField(max_length=32)
    #languages = forms.ModelChoiceField(queryset=Language.objects.all())
#    language = forms.ModelChoiceField(queryset=Language.objects.all())


def registrar(request):
    submitted = False
    if request.method == 'POST':
        form = RegistrarForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # assert False
            return HttpResponseRedirect('/registrar?submitted=True')
    else:
        form = RegistrarForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'djapp/registrar.html', {'form': form, 'submitted': submitted})
