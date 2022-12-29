from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from .models import Film, Ocena


class Aktor(models.Model):
     id = models.IntegerField(max_length=30)
     imie = models.CharField(max_length=30)
     nazwisko = models.CharField(max_length=30)

class Rezyser(models.Model):
    id = models.IntegerField(max_length=30)
    imie = models.CharField(max_length=30)
    nazwisko = models.CharField(max_length=30)

class Film(models.Model):
    id = models.IntegerField(max_length=30)
    nazwa = models.CharField(max_length=50)
    opis = models.CharField(max_length=100)
    aktor = models.ManyToManyField(Aktor)
    rezyser = models.ForeignKey(Rezyser, on_delete=models.CASCADE)
    ocena = models.ManyToOneRel(Ocena)
    utworzony = models.CharField(max_length=30)
    zaktualizowany = models.CharField(max_length=30)

    def no_of_rating(self):
        ocena = Ocena.objects.filter(film=self)
        return len(ocena)

    def mean_rating(self):
        ocena = Ocena.objects.filter(film=self)
        sums = 0
        mean = 0
        for ocena in ocena:
            sums = sums + ocena.gwiazdki
        if sums != 0:
            mean = sums / len(ocena)
            return mean
        else:
            return mean


class Ocena(models.Model):
    id = models.IntegerField(max_length=30)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    ocena = models.IntegerField(max_length=30)
    uzytkownik = models.ForeignKey(User, on_delete=models.CASCADE)
    gwiazdki = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)], null=False, blank=False)



    class Meta:
        unique_together = {('uzytkownik', 'film')}
        index_together = {('uzytkownik', 'film')}
        ordering = {'-gwiazdki'}