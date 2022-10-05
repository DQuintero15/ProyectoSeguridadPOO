from django.contrib import admin
from .models.ModeloArma import ModeloArma
from .models.FuerzaMilitar import FuerzaMilitar
from .models.RangoMilitar import RangoMilitar
from .models.Militar import Militar
from .models.Arma import Arma
from .models.ModeloArma import ModeloArma
from .models.DivisionMilitar import DivisionMilitar
from .models.UbicacionMilitar import UbicacionMilitar
from .models.InstalacionMilitar import InstalacionMilitar
from .models.Poligono import Poligono
from .models.PracticaPoligono import PracticaPoligono

admin.site.register(FuerzaMilitar)
admin.site.register(RangoMilitar)
admin.site.register(Arma)
admin.site.register(Militar)
admin.site.register(ModeloArma)
admin.site.register(DivisionMilitar)
admin.site.register(UbicacionMilitar)
admin.site.register(InstalacionMilitar)
admin.site.register(Poligono)
admin.site.register(PracticaPoligono)
