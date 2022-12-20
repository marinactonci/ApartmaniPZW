from django.db import transaction
from django.core.management.base import BaseCommand
from main.models import Apartman, Gost, Rezervacija
from main.factory import ApartmanFactory, GostFactory, RezervacijaFactory

NUM_APARTMANS = 100
NUM_GOSTS = 100
NUM_REZERVACIJAS = 100
class Command(BaseCommand):
    help = "This command generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):

        self.stdout.write("Deleting old data...")
        models = [Apartman, Gost, Rezervacija]
        for model in models:
            model.objects.all().delete()

        self.stdout.write("Creating new data...")
        for i in range(NUM_APARTMANS):
            ApartmanFactory()

        for i in range(NUM_GOSTS):
            GostFactory()

        for i in range(NUM_REZERVACIJAS):
            RezervacijaFactory()
