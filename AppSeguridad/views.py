from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from FuerzasMilitares.models.Militar import Militar
from FuerzasMilitares.models.UbicacionMilitar import UbicacionMilitar
from django import template
from FuerzasMilitares.models.RangoMilitar import RangoMilitar
from FuerzasMilitares.models.InstalacionMilitar import InstalacionMilitar
from FuerzasMilitares.models.Arma import Arma

register = template.Library()


@login_required(login_url="/accounts/login")
def cerberus_home(request):
    return render(request, "index.html")


@login_required(login_url="/accounts/login")
def profile(request):
    if request.user.is_authenticated:
        return render(request, "profile.html")


@login_required(login_url="/accounts/login")
def esquema_proteccion_view(request):
    if request.user.is_authenticated:
        return render(request, "esquema_seguridad.html")


@login_required(login_url="/accounts/login")
def personal(request):
    if request.user.is_authenticated:
        user_id = request.user.id
        id_militar = Militar.objects.get(usuario_id=user_id).id_militar
        id_instalacion = InstalacionMilitar.objects.get(
            id_instalacion=id_militar
        ).id_instalacion

        militares = (
            UbicacionMilitar.objects.select_related("militar")
            .select_related("instalacion")
            .filter(instalacion_id=id_instalacion)
        )
        context = {"militares": militares}
    return render(request, "personal.html", context)


@login_required(login_url="/accounts/login")
def armamento(request):
    if request.user.is_authenticated:
        armas = Arma.objects.select_related("modelo")
        context = {"armas": armas}
        return render(request, "armamento.html", context)
