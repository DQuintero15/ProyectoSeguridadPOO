from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as login_user, logout as logout_user
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login_user(request, user)
            return redirect("/cerberus/")
        else:
            messages.error(request, "Nombre de usuario o contraseña no válidos")
            return redirect("/accounts/login/")
    return render(request, "login.html", {})


def logout(request):
    logout_user(request)
    return redirect("/accounts/login")
