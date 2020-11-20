from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
# from django.http import HttpResponse

from clients.models import Client


def home(request):
    """Home page view."""
    return render(
        # request, 'homepage/home.html',
        request, 'homepage/index.html',
    )


@login_required
def my_businesses(request):
    """Businesses Dashboard.

    First, check whether the user is a client or employee.
    Different dashboards are displayed depending on the user
    """
    user_type = None
    user = request.user
    try:
        client = Client.objects.get(user=user)
        if client:
            user_type = "Client"
    except ObjectDoesNotExist:
        user_type = "Employee"
    context = {
        "user_type": user_type
    }

    return render(
        request, 'homepage/index_businesses.html',
        context
    )
