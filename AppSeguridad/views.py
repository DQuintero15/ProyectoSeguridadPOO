from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from FuerzasMilitares.models.Militar import Militar
from FuerzasMilitares.models.PracticaPoligono import (
    PracticaPoligono,
    PracticaPoligoForm,
)
from FuerzasMilitares.models.UbicacionMilitar import UbicacionMilitar
from django import template
from FuerzasMilitares.models.InstalacionMilitar import InstalacionMilitar
from FuerzasMilitares.models.Arma import Arma
from FuerzasMilitares.models.Poligono import PoligoForm, Poligono
from django.shortcuts import HttpResponseRedirect
from .Functions import DetectorObjetivos


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


def practica_poligono(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PracticaPoligoForm(request.POST)
            if form.is_valid():
                # Datos generales
                id_militar = Militar.objects.get(usuario_id=request.user.id).id_militar
                id_instalacion = InstalacionMilitar.objects.get(
                    id_instalacion=id_militar
                ).id_instalacion

                fecha = request.POST.get("fecha")
                modelo_objetivo = request.POST.get("modelo_objetivo")
                disponible = bool(request.POST.get("disponible"))

                practica_poligono = PracticaPoligono(
                    None, fecha, id_instalacion, disponible, modelo_objetivo, id_militar
                )

                practica_poligono.save()

                return HttpResponseRedirect("/cerberus/poligono/")

        else:
            form = PracticaPoligoForm()
        return render(request, "practica_poligono.html", {"form": form})


def poligono(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PoligoForm(request.POST)
            if form.is_valid():
                arma = request.POST.get("arma")
                provedores = request.POST.get("provedores")
                cartuchos = request.POST.get("cartuchos")
                distancia = request.POST.get("distancia")
                objetivo = request.POST.get("objetivo")
                practica_poligono = request.POST.get("practica_poligono")

                id_militar = Militar.objects.get(
                    usuario_id=request.user.id
                ).id_militar

                poligono = Poligono(
                    None,
                    arma,
                    provedores,
                    cartuchos,
                    distancia,
                    objetivo,
                    practica_poligono,
                )
                # poligono.save()

                plantilla = PracticaPoligono.objects.get(
                    id_practica_poligono=poligono.practica_poligono.id_practica_poligono
                ).modelo_objetivo.url

                porcentaje = DetectorObjetivos.DetectorObjetivos.procesarImagenes(
                    plantilla, objetivo
                )
                print(porcentaje)

                return HttpResponseRedirect("/cerberus/poligono/")

        else:
            form = PoligoForm()
        return render(request, "registro_poligono.html", {"form": form})
