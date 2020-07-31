from django.urls import path

from . import views

app_name = "rental_houses"

urlpatterns = [
    path('', views.index, name="rental_houses_home"),
    path('my-premises/', views.my_premises, name="my_property"),
    path('add-premises/', views.add_premises, name="add_appartment"),
    path(
        'premises/<slug:premises_id>/', views.view_premises,
        name="view_premises"
    ),
    path(
        'premises/<slug:premises_id>/add-a-house/',
        views.add_house_to_premises,
        name="add_house"
    ),
    path(
        'premises/<slug:premises_id>/units/', views.view_premises_units,
        name="view_premises_houses"
    ),
    path(
        'premises/<slug:premises_id>/units/<slug:unit_id>/',
        views.view_single_unit, name="view_single_unit"
    ),
    path(
        'premises/<slug:premises_id>/units/<slug:unit_id>/rent/add-payment/',
        views.add_rent_payment, name="add_rent_payment"
    )
]
