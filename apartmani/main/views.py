from django.shortcuts import render
from django.views.generic import ListView
from main.models import Apartman, Gost, Rezervacija
# Create your views here.
def homepage(request):
    return render(request, "index.html")

class ApartmanList(ListView):
    model = Apartman

class GostList(ListView):
    model = Gost

class RezervacijaList(ListView):
    model = Rezervacija