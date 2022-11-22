from functools import reduce
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
from AppSeguridad.models.IntegranteEsquemaSeguridad import (
    IntegranteEsquemaSeguridadForm,
    IntegranteEsquemaSeguridad,
)
from AppSeguridad.models.EsquemaSeguridad import EsquemaSeguridadForm
from django.contrib import messages
from .Functions import WebScrapping
import requests
from bs4 import BeautifulSoup

register = template.Library()


@login_required(login_url="/accounts/login")
def cerberus_home(request):
    user = request.user
    if user.is_authenticated:
        request_page = requests.get("https://cnnespanol.cnn.com/category/seguridad/")
        if request_page.status_code == 200:  # Solicitud completada
            contenido = BeautifulSoup(request_page.text, "lxml")

            noticias = contenido.find(
                "div", attrs={"class": "module__content row--container"}
            ).find_all("article")

            context = {}

            for noticia in noticias:
                titulo = noticia.a.get("title")
                imagen_url = noticia.a.img.get("data-lazy-src")
                url_noticia = noticia.a.get("href")
                context[titulo] = [imagen_url, url_noticia]

    return render(request, "index.html", {"noticias": context})


@login_required(login_url="/accounts/login")
def profile(request):
    if request.user.is_authenticated:
        return render(request, "profile.html")


integrantes = []


@login_required(login_url="/accounts/login")
def esquema_proteccion_view(request):
    user = request.user
    if user.is_authenticated:
        if request.method == "GET":
            return render(
                request,
                "esquema_seguridad.html",
                {
                    "form": IntegranteEsquemaSeguridadForm(),
                },
            )
        if request.method == "POST":

            if "iniciar_planeacion" in request.POST and len(integrantes) > 0:
                return HttpResponseRedirect(
                    "/cerberus/registrar-esquema/",
                    {
                        "integrantes": integrantes,
                    },
                )

            form = IntegranteEsquemaSeguridadForm(request.POST)
            militar = str(request.POST.get("militar"))
            arma = str(request.POST.get("arma"))
            tarea = str(request.POST.get("tarea"))

            if form.is_valid():
                integrate_esquema = IntegranteEsquemaSeguridad(
                    None, arma, militar, tarea
                )

                def getName(integrante):
                    return integrante.militar.nombres

                nombreActual = getName(integrate_esquema)
                listado_nombres = set(map(lambda x: getName(x), integrantes))

                if nombreActual not in listado_nombres:
                    integrantes.append(integrate_esquema)

                    messages.error(
                        request,
                        "Ingresado satisfactoriamente",
                    )
                return render(
                    request,
                    "esquema_seguridad.html",
                    {
                        "integrantes": integrantes,
                        "form": IntegranteEsquemaSeguridadForm(),
                    },
                )

            else:
                # Error message
                pass

        form = IntegranteEsquemaSeguridadForm()
        return render(
            request,
            "esquema_seguridad.html",
            {"form": form},
        )


@login_required(login_url="/accounts/login")
def registro_esquema_view(request):
    user = request.user
    if user.is_authenticated:
        form = EsquemaSeguridadForm()
        if request.method == "POST":

            return render(request, "registro_esquema.html", {"form": form})
        else:
            form = EsquemaSeguridadForm()
        return render(request, "registro_esquema.html", {"form": form})


@login_required(login_url="/accounts/login")
def personal(request):
    return render(request, "personal.html")


@login_required(login_url="/accounts/login")
def armamento(request):
    if request.user.is_authenticated:
        armas = Arma.objects.select_related("modelo")
        context = {"armas": armas}
        return render(request, "armamento.html", context)


@login_required(login_url="/accounts/login")
def practica_poligono(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PracticaPoligoForm(request.POST, request.FILES)
            fecha = request.POST.get("fecha")

            disponible = bool(request.POST.get("disponible"))
            modelo_objetivo = request.FILES["modelo_objetivo"]
            if form.is_valid():
                # Datos generales
                id_militar = Militar.objects.get(usuario_id=request.user.id).id_militar
                id_instalacion = InstalacionMilitar.objects.get(
                    id_instalacion=id_militar
                ).id_instalacion

                practica_poligono = PracticaPoligono(
                    None, fecha, id_instalacion, disponible, modelo_objetivo, id_militar
                )

                practica_poligono.save()

                return HttpResponseRedirect("/cerberus/poligono/")

        else:
            form = PracticaPoligoForm()
        return render(request, "practica_poligono.html", {"form": form})


@login_required(login_url="/accounts/login")
def poligono(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PoligoForm(request.POST, request.FILES)
            arma = request.POST.get("arma")
            provedores = request.POST.get("provedores")
            cartuchos = request.POST.get("cartuchos")
            distancia = request.POST.get("distancia")
            objetivo = request.FILES["imagen_objetivo"]
            practica_poligono = request.POST.get("practica_poligono")
            if form.is_valid():
                id_militar = Militar.objects.get(usuario_id=request.user.id).id_militar

                poligono = Poligono(
                    None,
                    arma,
                    provedores,
                    cartuchos,
                    distancia,
                    objetivo,
                    practica_poligono,
                    id_militar,
                    None,
                    None,
                )

                poligono.save()

                plantilla = str(
                    PracticaPoligono.objects.get(
                        id_practica_poligono=poligono.practica_poligono.id_practica_poligono
                    ).modelo_objetivo.url
                )

                objetivo_impactos = str(
                    Poligono.objects.get(
                        id_poligono=poligono.id_poligono
                    ).imagen_objetivo.url
                )

                plantilla = plantilla.split("/")
                plantilla = plantilla[len(plantilla) - 1]
                url_objetivo = objetivo_impactos.split("/")[4]

                url_plantilla = f"media\images\modelos\{plantilla}"
                url_objetivo = f"media\images\poligonos\{url_objetivo}"

                estadisticas = DetectorObjetivos.DetectorObjetivos.procesarImagenes(
                    url_plantilla, url_objetivo
                )

                print("Porcentaje de efectividad: ", estadisticas["efectivdad"])
                print("Cantidad aproximada de aciertos: ", estadisticas["n_impactos"])

                poligono.n_impactos = int(estadisticas["n_impactos"])
                poligono.prom_efectividad = float(estadisticas["efectivdad"])

                poligono.save()

                return HttpResponseRedirect("/cerberus/poligono/")

        else:
            form = PoligoForm()
        return render(request, "registro_poligono.html", {"form": form})


@login_required(login_url="/accounts/login")
def mis_poligonos_view(request):
    if request.user.is_authenticated:
        id_militar = Militar.objects.get(usuario_id=request.user.id).id_militar
        poligonos = Poligono.objects.filter(militar_id=id_militar)
        context = {"poligonos": poligonos}
        return render(request, "mis_poligonos.html", context)


@login_required(login_url="/accounts/login")
def mis_estadisticas_view(request):
    if request.user.is_authenticated:
        id_militar = Militar.objects.get(usuario_id=request.user.id).id_militar
        poligonos = Poligono.objects.filter(militar_id=id_militar)

        impactos = poligonos.values_list("n_impactos", flat=True)
        efectividad = poligonos.values_list("prom_efectividad", flat=True)

        n_poligonos = len(impactos)
        promedio_impactos = reduce(lambda acc, el: acc + el, impactos) // n_poligonos
        promedio_efectividad = (
            reduce(lambda acc, el: acc + el, efectividad) // n_poligonos
        )
        mejor_practica = poligonos.order_by("-prom_efectividad").first()
        context = {
            "promedio_impactos": promedio_impactos,
            "promedio_efectividad": promedio_efectividad,
            "n_poligonos": n_poligonos,
            "mejor_practica": mejor_practica,
        }

        return render(request, "mis_estadisticas.html", context)


@login_required(login_url="/accounts/login")
def mi_instalacion_view(request):
    return render(request, "informacion_instalacion.html")


@login_required(login_url="/accounts/login")
def FAQ_view(request):
    return render(request, "FAQ.html")


@login_required(login_url="/accounts/contacto")
def contacto_view(request):
    return render(request, "contacto.html")
