from django.urls import path
from . import views

urlpatterns = [
    path("", view=views.home),
    path(r"^/(?P<token>\w{0,50})/$", view=views.home),
]
