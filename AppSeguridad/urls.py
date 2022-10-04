from django.urls import path
from . import views

urlpatterns = [
    path("", views.cerberus_home),
    path("profile/", views.profile),
    path("esquema/", views.esquema_proteccion_view),
    path("personal/", views.personal),
    path("armamento/", views.armamento),
]
