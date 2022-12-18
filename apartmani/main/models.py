from django.db import models

# Create your models here.


class Apartman(models.Model):
    ime = models.CharField(max_length=50)
    adresa = models.CharField(max_length=50)
    cijena_noci = models.IntegerField(max_length=3)
    max_gosti = models.IntegerField(max_length=2)
    min_br_nocenja = models.IntegerField(max_length=2)

    def __str__(self):
        return self.ime


class Gost(models.Model):
    ime = models.CharField(max_length=50)
    prezime = models.CharField(max_length=50)
    drzava = models.CharField(max_length=30)
    grad = models.CharField(max_length=50)
    oib = models.IntegerField(max_length=11)

    def __str__(self):
        return self.ime, self.prezime


class Rezervacija(models.Model):
    gost = models.ForeignKey(Gost, on_delete=models.CASCADE)
    apartman = models.OneToOneField(Apartman, on_delete=models.CASCADE)
    datum_od = models.DateField()
    datum_do = models.DateField()
    broj_nocenja = models.IntegerField(max_length=2)
    cijena_ukupno = models.IntegerField(max_length=5)