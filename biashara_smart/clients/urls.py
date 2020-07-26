from django.urls import path

from . import views

urlpatterns = [
    path('signup/', views.client_signup, name="client_signup"),
    path('login/', views.client_login, name="client_login"),
]
