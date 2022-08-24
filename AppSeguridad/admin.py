from django.contrib import admin
from .models import Arma
from .models import Protegido

admin.site.register(Protegido)
admin.site.register(Arma)