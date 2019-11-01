from django.db import models


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

    name = models.CharField(max_length=32)
    country = models.IntegerField(choices=COUNTRIES)
    city = models.CharField(max_length=32)
    language = models.ManyToManyField(Language)
    t_and_c = models.BooleanField(default=False, verbose_name="Accept terms and conditions")

    class Meta:
        app_label = 'djapp'



