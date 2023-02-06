from main.models import Apartman
from django.test import TestCase

class TestApartman(TestCase):
    def setUp(self):
        Apartman.objects.create(
            ime="Apartman 1",
            adresa="Address 1",
            cijena_noci=50,
            max_gosti=4,
            min_br_nocenja=3,
            broj_zvezdica=3
        )
        Apartman.objects.create(
            ime="Apartman 2",
            adresa="Address 2",
            cijena_noci=60,
            max_gosti=6,
            min_br_nocenja=2,
            broj_zvezdica=4
        )

    def test_apartman_string_representation(self):
        apartman_1 = Apartman.objects.get(ime="Apartman 1")
        apartman_2 = Apartman.objects.get(ime="Apartman 2")
        self.assertEqual(str(apartman_1), "Apartman 1")
        self.assertEqual(str(apartman_2), "Apartman 2")

    def test_apartman_max_gosti(self):
        apartman_1 = Apartman.objects.get(ime="Apartman 1")
        apartman_2 = Apartman.objects.get(ime="Apartman 2")
        self.assertEqual(apartman_1.max_gosti, 4)
        self.assertEqual(apartman_2.max_gosti, 6)

    def test_apartman_cijena_noci(self):
        apartman_1 = Apartman.objects.get(ime="Apartman 1")
        apartman_2 = Apartman.objects.get(ime="Apartman 2")
        self.assertEqual(apartman_1.cijena_noci, 50)
        self.assertEqual(apartman_2.cijena_noci, 60)
