from django.urls import path, include
from . import views
from main.views import ApartmanList, GostList, RezervacijaList

app_name="main"

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('apartments', ApartmanList.as_view()),
    path('main/<int:pk>/', views.apartman_detail, name='apartman_detail'),
    path('gosti', GostList.as_view()),
    path('rezervacije', RezervacijaList.as_view()),
    path('register', views.register_request, name="register"),
    path('login', views.login_request, name="login"),
    path('logout', views.logout_request, name="logout"),
    path('contact', views.contact, name="contact")
]
