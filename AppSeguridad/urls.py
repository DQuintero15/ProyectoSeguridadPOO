from django.urls import path
from . import views

urlpatterns = [
    path("", views.cerberus_home),
    path("profile/", views.profile),
    path("esquema/", views.esquema_proteccion_view),
    path("personal/", views.personal),
    path("armamento/", views.armamento),
    path("practica-poligono/", views.practica_poligono),
    path("poligono/", views.poligono),
    path("mis-poligonos/", views.mis_poligonos_view),
    path("mis-estadisticas/", views.mis_estadisticas_view),
    path("mi-instalacion/", views.mi_instalacion_view),
    path("registrar-esquema/", views.registro_esquema_view),
    path("FAQ/", views.FAQ_view),
    path("contacto/", views.contacto_view),
]
