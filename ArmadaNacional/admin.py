from django.contrib import admin
from .models.InfanteMarina import InfanteMarina
from .models.ArmadaNacional import BrigadaArmadaNacional
from .models.ArmadaNacional import BatallonInfanteria

admin.site.register(InfanteMarina)
admin.site.register(BatallonInfanteria)
admin.site.register(BrigadaArmadaNacional)
