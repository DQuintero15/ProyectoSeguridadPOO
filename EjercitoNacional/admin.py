from django.contrib import admin
from .models import DivisonEjercitoNacional
from .models import BatallonEjercito
from .models import BrigadaUnidadEjercitoNacional
from .models import MilitarEjercito

admin.site.register(DivisonEjercitoNacional)
admin.site.register(BatallonEjercito)
admin.site.register(BrigadaUnidadEjercitoNacional)
admin.site.register(MilitarEjercito)



