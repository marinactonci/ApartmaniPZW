from django.db import models

# Create your models here.


class Apartman(models.Model):
    ime = models.CharField(max_length=50)
    adresa = models.CharField(max_length=50)
    cijena_noci = models.IntegerField()
    max_gosti = models.IntegerField()
    min_br_nocenja = models.IntegerField()
    broj_zvezdica = models.IntegerField()

    def __str__(self):
        return self.ime


class Gost(models.Model):
    ime = models.CharField(max_length=50)
    prezime = models.CharField(max_length=50)
    drzava = models.CharField(max_length=30)
    grad = models.CharField(max_length=50)
    oib = models.IntegerField()

    def __str__(self):
        return self.prezime


class Rezervacija(models.Model):
    datum_od = models.DateField()
    datum_do = models.DateField()
    broj_nocenja = models.IntegerField()
    cijena_ukupno = models.IntegerField()
    gost = models.OneToOneField(Gost, on_delete=models.CASCADE)
    apartman = models.ForeignKey(Apartman, on_delete=models.CASCADE)