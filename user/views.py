from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as login_user, logout as logout_user

    
def login(request):
    if request.method == "POST":
        username = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login_user(request, user)
            return redirect("/cerberus/")
    return render(request, "login.html")

def logout(request):
    logout_user(request)
    return redirect("/accounts/login")


