from django.db import models
from django.urls import reverse

class Projekt(models.Model):
    Tytul = models.CharField(max_length=100)
    podtytul = models.CharField(max_length=100)

    def __str__(self):
        return self.Tytul


class Okno(models.Model):
    projekt = models.ForeignKey(Projekt, on_delete=models.CASCADE)
    naglowek = models.CharField(max_length=200)
    zawartosc = models.TextField()

    def __str__(self):
        return self.naglowek
