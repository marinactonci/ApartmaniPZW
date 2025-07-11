import factory
from factory.django import DjangoModelFactory
from main.models import Gost, Apartman, Rezervacija

class ApartmanFactory(DjangoModelFactory):
    class Meta:
        model = Apartman

    ime = factory.Faker("first_name")
    adresa = factory.Faker("address")
    cijena_noci = factory.Faker('pyint', min_value=60, max_value=90)
    max_gosti = factory.Faker('pyint', min_value=1, max_value=4)
    min_br_nocenja = factory.Faker('pyint', min_value=1, max_value=10)
    broj_zvezdica = factory.Faker('pyint', min_value=1, max_value=5)

class GostFactory(DjangoModelFactory):
    class Meta:
        model = Gost

    ime = factory.Faker("first_name")
    prezime = factory.Faker("last_name")
    drzava = factory.Faker("country")
    grad = factory.Faker("city")
    oib = factory.Faker('pyint', min_value=10000000000, max_value=99999999999)

class RezervacijaFactory(DjangoModelFactory):
    class Meta:
        model = Rezervacija

    gost = factory.Iterator(Gost.objects.all())
    apartman = factory.Iterator(Apartman.objects.all())
    datum_od = factory.Faker("date_time")
    datum_do = factory.Faker("date_time")
    broj_nocenja = factory.Faker('pyint', min_value=1, max_value=10)
    cijena_ukupno = factory.Faker('pyint', min_value=60, max_value=360)