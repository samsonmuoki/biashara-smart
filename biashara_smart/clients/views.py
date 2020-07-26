from django.shortcuts import render

from django.http import HttpResponse


def client_signup(request):
    """Sign view up for clients."""
    # return HttpResponse("Welcome to Biashara smart")
    return render(
        request, 'clients/signup.html'
    )


def client_login(request):
    """Login view for clients."""
    return HttpResponse("Feature comming soon.")
