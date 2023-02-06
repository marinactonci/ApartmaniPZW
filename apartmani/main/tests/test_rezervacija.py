from django.test import TestCase
from django.utils.dateparse import parse_date
from main.models import Rezervacija, Apartman, Gost

class TestRezervacija(TestCase):
    def test_rezervacija_create(self):
        apartman = Apartman.objects.create(
            ime="Apartman 1",
            adresa="Address 1",
            cijena_noci=50,
            max_gosti=4,
            min_br_nocenja=3,
            broj_zvezdica=3
        )
        gost = Gost.objects.create(
            ime="First",
            prezime="Last",
            drzava="Country",
            grad="City",
            oib=123456789
        )
        rezervacija = Rezervacija.objects.create(
            datum_od=parse_date("2023-01-01"),
            datum_do=parse_date("2023-01-03"),
            broj_nocenja=2,
            cijena_ukupno=100,
            gost=gost,
            apartman=apartman
        )
        self.assertEqual(rezervacija.datum_od, parse_date("2023-01-01"))
        self.assertEqual(rezervacija.datum_do, parse_date("2023-01-03"))
        self.assertEqual(rezervacija.broj_nocenja, 2)
        self.assertEqual(rezervacija.cijena_ukupno, 100)
        self.assertEqual(rezervacija.gost, gost)
        self.assertEqual(rezervacija.apartman, apartman)