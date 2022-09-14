from django.contrib import admin
from .models.Armamento import ModeloArma
from .models.Armamento import Arma
from .models.Visitante import Visitante

admin.site.register(ModeloArma)
admin.site.register(Arma)
admin.site.register(Visitante)
