from django.urls import path
from djapp.views import RegistrationView

app_name = 'djapp'

urlpatterns = [
    path('', RegistrationView.as_view()),
]
