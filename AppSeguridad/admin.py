from django.contrib import admin
from .models import Arma
from .models import Militar
from .models import Visitante
from .models import Posicion
from .models import Vehiculo
from .models import Batallon

admin.site.register(Arma)
admin.site.register(Militar)
admin.site.register(Posicion)
admin.site.register(Visitante)
admin.site.register(Vehiculo)
admin.site.register(Batallon)