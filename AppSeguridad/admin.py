from django.contrib import admin
from .models import Arma
from .models import Protegido
from .models import Escolta

admin.site.register(Protegido)
admin.site.register(Arma)
admin.site.register(Escolta)