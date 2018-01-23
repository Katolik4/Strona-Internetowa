from django.db import models
from django.urls import reverse


class Urzadzenie(models.Model):
    nr_ser = models.CharField(max_length=100)
    Nazwa = models.CharField(max_length=250)
    Seria = models.CharField(max_length=250)

    def get_absolute_url(self):
        return  reverse('esp:detail', kwargs={'pk': self.pk})
    def __str__(self):
        return self.Nazwa +' - '+self.Seria

class Gpio(models.Model):
    urzadzenie = models.ForeignKey(Urzadzenie, on_delete=models.CASCADE)
    stan = models.CharField(max_length=250)
    opis = models.CharField(max_length=250, default="")
    lista = models.CharField(max_length=250, default="")
    bolean = models.BooleanField(default=False)


    def get_absolute_url(self):
        return  reverse(('esp:gpio-update'), kwargs={'pk_urzadzenie': self.urzadzenie.pk, 'pk': self.pk})
    def __str__(self):
        return self.opis +' - Urzadzenie: '+self.urzadzenie.Nazwa
