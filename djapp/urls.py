from django.urls import path
from djapp.views import RegistrationView
#from . import registration

urlpatterns = [
    path('', RegistrationView.as_view(), name='registrar'),
]
