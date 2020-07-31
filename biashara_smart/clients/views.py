from django.shortcuts import (
    render,
    # get_object_or_404,
    redirect,
)

from django.http import (
    HttpResponse,
)
from django.contrib.auth import login, authenticate, logout

from .forms import ClientSignUpForm, ClientLoginForm
from .models import Client


def client_signup(request):
    """Sign view up for clients."""
    if request.method == 'POST':
        form = ClientSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')

            user = authenticate(username=username, password=password)
            login(request, user)

            # create a client record corresponding to the newly created user
            client = request.user
            Client.objects.get_or_create(
                user=client,
                defaults={
                    "first_name": first_name,
                    "last_name": last_name,
                    "phone_number": username,
                    "email": email,
                    "user": request.user,
                },
            )

            return redirect('homepage:my_businesses')
    else:
        form = ClientSignUpForm()
    return render(request, 'clients/client_signup.html', {'form': form})


def client_login(request):
    """Login view for clients."""
    if request.method == "POST":
        form = ClientLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['phone_number']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                return redirect('homepage:my_businesses')
            else:
                return HttpResponse("Invalid username or password")
    else:
        form = ClientLoginForm()
    return render(
        request, 'clients/client_login.html',
        {'form': form}
    )


def client_logout(request):
    """Log out a logged in client."""
    logout(request)
    return redirect('homepage:homepage')
