from django.urls import path, include
from . import views
from main.views import ApartmanList, GostList, RezervacijaList
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView

app_name="main"

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('apartments', ApartmanList.as_view()),
    path('main/<int:pk>/', views.apartman_detail, name='apartman_detail'),
    path('gosti', GostList.as_view()),
    path('rezervacije', RezervacijaList.as_view()),
    path('accounts/register', views.register_request, name="register"),
    path('accounts/login/', views.login_request, name="login"),
    path('accounts/logout', views.logout_request, name="logout"),
    path('contact', views.contact, name="contact"),
    path('profile', views.profile, name="profile"),
    path('password_change', PasswordChangeView.as_view(), name='password_change'),
    path('password_change_done/', PasswordChangeDoneView.as_view(), name='password_change_done')
]
