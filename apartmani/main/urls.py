from django.urls import path, include
from . import views
from main.views import ApartmanList, GostList, RezervacijaList

app_name="main"

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('apartmani', ApartmanList.as_view()),
    path('gosti', GostList.as_view()),
    path('rezervacije', RezervacijaList.as_view())
]
