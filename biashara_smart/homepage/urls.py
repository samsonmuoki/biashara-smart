from django.urls import path

from . import views

app_name = "homepage"

urlpatterns = [
    path('', views.home, name="homepage"),
    path('my-businesses', views.my_businesses, name="my_businesses"),
]
