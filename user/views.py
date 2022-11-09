from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as login_user, logout as logout_user
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from core.settings import RECAPTCHA_PUBLIC_KEY


def login_view(request):
    if request.method == "GET" and request.user.is_authenticated:
        return redirect("/cerberus/")
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        context = {"site_key": RECAPTCHA_PUBLIC_KEY}

        if user is not None:
            login_user(request, user)
            return redirect("/cerberus/")
        else:
            messages.error(request, "Nombre de usuario o contraseña no válidos")
            return redirect("/accounts/login/", context)
    return render(request, "login.html", {})


@login_required(login_url="/accounts/login/")
def logout(request):
    logout_user(request)
    return redirect("/accounts/login", {})
