from django.shortcuts import render


def eror_404(request, exception):
    return render(
        request,
        "404.html",
    )
