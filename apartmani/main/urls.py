from django.urls import path, include
from . import views
from main.views import ApartmanList, GostList, RezervacijaList, ApartmentPage

app_name="main"

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('apartments', ApartmanList.as_view()),
    path('main/<int:pk>/', ApartmentPage.as_view(), name='apartman_detail'),
    path('gosti', GostList.as_view()),
    path('rezervacije', RezervacijaList.as_view()),
    path('register', views.register_request, name="register"),
    path('login', views.login_request, name="login"),
    path('logout', views.logout_request, name="logout")
]
