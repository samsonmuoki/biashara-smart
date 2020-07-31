from django.urls import path

from . import views

app_name = "clients"

urlpatterns = [
    path('signup/', views.client_signup, name="client_signup"),
    path('login/', views.client_login, name="client_login"),
    path('logout/', views.client_logout, name="client_logout"),
]
