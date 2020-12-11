from django.urls import path, include
from rest_framework import routers

from . import views, models

app_name = "clients"

router = routers.DefaultRouter()
router.register(
    r'owners_api', views.OwnerViewSet, basename=models.Client
)

urlpatterns = [
    path('', include(router.urls)),
    path('signup/', views.client_signup, name="client_signup"),
    path('login/', views.client_login, name="client_login"),
    path('logout/', views.client_logout, name="client_logout"),
]
