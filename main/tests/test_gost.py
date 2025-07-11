from django.test import TestCase
from main.models import Gost

class TestGost(TestCase):
    def test_gost_create(self):
        gost = Gost.objects.create(
            ime="First",
            prezime="Last",
            drzava="Country",
            grad="City",
            oib=123456789
        )
        self.assertEqual(gost.ime, "First")
        self.assertEqual(gost.prezime, "Last")
        self.assertEqual(gost.drzava, "Country")
        self.assertEqual(gost.grad, "City")
        self.assertEqual(gost.oib, 123456789)
