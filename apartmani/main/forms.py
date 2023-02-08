from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Gost, Rezervacija


# Create your forms here.

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea,
                              max_length=2000, required=True)


class GostForm(forms.ModelForm):
    class Meta:
        model = Gost
        fields = ['ime', 'prezime', 'drzava', 'grad', 'oib']
        labels = {
            'ime': 'First Name',
            'prezime': 'Last Name',
            'drzava': 'Country',
            'grad': 'City',
            'oib': 'OIB',
        }


class RezervacijaForm(forms.ModelForm):
    class Meta:
        model = Rezervacija
        fields = ['datum_od', 'datum_do']
        labels = {
            'datum_od': 'Date from',
            'datum_do': 'Date to'
        }
        widgets = {
            'datum_od': forms.DateInput(attrs={'type': 'date'}),
            'datum_do': forms.DateInput(attrs={'type': 'date'}),
        }