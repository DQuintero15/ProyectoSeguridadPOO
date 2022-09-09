from django.contrib import admin
from .models import Arma
from .models import Militar
from .models import Visitante
from .models import Posicion


admin.site.register(Arma)
admin.site.register(Militar)
admin.site.register(Posicion)
admin.site.register(Visitante)