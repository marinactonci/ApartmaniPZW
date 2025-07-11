from django.contrib import admin
from main.models import *
# Register your models here.
model_list = [Apartman, Gost, Rezervacija]
admin.site.register(model_list)