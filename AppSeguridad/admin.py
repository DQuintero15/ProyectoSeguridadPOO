from django.contrib import admin
from .models.Visitante import Visitante
from .models.Vehiculo import Vehiculo
from .models.EsquemaSeguridad import EsquemaSeguridad
from .models.IntegranteEsquemaSeguridad import IntegranteEsquemaSeguridad

admin.site.register(Vehiculo)
admin.site.register(Visitante)
admin.site.register(EsquemaSeguridad)
admin.site.register(IntegranteEsquemaSeguridad)
