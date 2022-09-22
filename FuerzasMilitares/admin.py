from django.contrib import admin

from FuerzasMilitares.models.ModeloArma import ModeloArma
from .models.FuerzaMilitar import FuerzaMilitar
from .models.RangoMilitar import RangoMilitar
from .models.Militar import Militar
from .models.Arma import Arma
from .models.ModeloArma import ModeloArma
from .models.BrigadaMilitar import BrigadaMilitar
from .models.Batallon import Batallon


admin.site.register(FuerzaMilitar)
admin.site.register(RangoMilitar)
admin.site.register(Arma)
admin.site.register(Militar)
admin.site.register(ModeloArma) 
admin.site.register(BrigadaMilitar)
admin.site.register(Batallon)
