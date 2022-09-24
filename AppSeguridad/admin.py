from django.contrib import admin
from .models.Visitante import Visitante
from .models.Vehiculo import Vehiculo
from .models.IntegranteEsquemaSeguridad import IntegranteEsquemaSeguridad
from .models.EsquemaSeguridad import EsquemaSeguridad

admin.site.register(Vehiculo)
admin.site.register(Visitante)
admin.site.register(EsquemaSeguridad)
admin.site.register(IntegranteEsquemaSeguridad)
