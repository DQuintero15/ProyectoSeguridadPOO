from django.conf import settings
from django.core.mail import EmailMessage
from django.http import HttpResponseRedirect
from django.shortcuts import render


def home(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        asunto = request.POST.get("asunto")
        correo_electronico = request.POST.get("correo_electronico")
        try:
            email = EmailMessage(
                subject=nombre,
                body=asunto,
                from_email=correo_electronico,
                to=[settings.RECIPIENT_ADDRESS],
            )
            email.send()
            return HttpResponseRedirect("/")
        except:
            pass
    return render(request, "home.html")
