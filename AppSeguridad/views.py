from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url="/accounts/login")
def cerberus_home(request):
    user = None
    if request.user.is_authenticated:
        user = request.user
        data = {}
        data['usuario'] = user
        return render(request, "index.html", data)
