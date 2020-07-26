from django.shortcuts import render

from django.http import HttpResponse


def home(request):
    """Home page."""
    return HttpResponse("LIQUOR SHOP MANAGEMENT")
