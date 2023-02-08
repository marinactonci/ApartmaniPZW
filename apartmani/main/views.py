from django.shortcuts import render, redirect
from django.views.generic import ListView
from main.models import Apartman, Gost, Rezervacija
from .forms import NewUserForm, ContactForm, GostForm, RezervacijaForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def homepage(request):
    return render(request, "index.html")


def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = "Website Inquiry" 
			body = {
			'first_name': form.cleaned_data['first_name'], 
			'last_name': form.cleaned_data['last_name'], 
			'email': form.cleaned_data['email'], 
			'message':form.cleaned_data['message'], 
			}
			message = "\n".join(body.values())

			try:
				send_mail(subject, message, 'fifijevcvijet@gmail.com', ['fifijevcvijet@gmail.com']) 
			except BadHeaderError:
				return messages.success(request, 'Invalid header found.')
			
			messages.success(request, 'Contact form successfully submitted!')

			return redirect ("main:homepage")
      
	form = ContactForm()
	return render(request, "contact.html", {'form':form})


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("main:homepage")
        messages.error(
            request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="registration/register.html", context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("main:homepage")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="registration/login.html", context={"login_form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("main:homepage")


class ApartmanList(ListView):
    model = Apartman


class GostList(ListView):
    model = Gost


class RezervacijaList(ListView):
    model = Rezervacija


def apartman_detail(request, pk):
    apartman = Apartman.objects.get(pk=pk)
    if request.method == 'POST':
        gost_form = GostForm(request.POST)
        rezervacija_form = RezervacijaForm(request.POST)
        if gost_form.is_valid() and rezervacija_form.is_valid():
            gost = gost_form.save()
            rezervacija = rezervacija_form.save(commit=False)
            rezervacija.gost = gost
            rezervacija.apartman = apartman
            rezervacija.broj_nocenja = (rezervacija.datum_do - rezervacija.datum_od).days
            rezervacija.cijena_ukupno = apartman.cijena_noci * rezervacija.broj_nocenja
            rezervacija.save()
            messages.success(request, "Successfully created the reservation!")
            return redirect('/apartments')
    else:
        gost_form = GostForm()
        rezervacija_form = RezervacijaForm()
    return render(request, 'main/apartman_detail.html', {'apartman': apartman, 'gost_form': gost_form, 'rezervacija_form': rezervacija_form})


@login_required
def profile(request):
    user = request.user
    context = {
        'username': user.username,
        'email': user.email,
        'date_joined': user.date_joined,
    }
    return render(request, 'registration/profile.html', context)
