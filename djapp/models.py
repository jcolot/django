from django.db import models
from django.utils.translation import ugettext_lazy as _

class Language(models.Model):
    name = models.CharField(max_length=32)

    class Meta:
        app_label = 'djapp'
        ordering = ['name']


    def __str__(self):
        return self.name


class Registrar(models.Model):
    COUNTRIES = (
        (1, 'France'),
        (2, 'Belgium'),
        (3, 'Germany')
    )

    name = models.CharField(max_length=32, verbose_name=_('name'))
    country = models.IntegerField(choices=COUNTRIES, verbose_name=_('country'))
    city = models.CharField(max_length=32, verbose_name=_('city'))
    language = models.ManyToManyField(Language, verbose_name=_('language'))
    t_and_c = models.BooleanField(default=False, verbose_name=_("Accept terms and conditions"))

    class Meta:
        app_label = 'djapp'



