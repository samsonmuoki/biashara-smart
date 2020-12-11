from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import (
    get_user,
    # get_user_model
)
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import APIView
from .serializers import (
    PremisesSerializer, UnitSerializer, RentPaymentSerializer,
    RentAccountSerializer,
)

from .forms import PremisesForm, UnitForm, RentPaymentForm
from .models import Premises, Unit, RentPayment, RentAccount
from common.views import AbstractBaseFilterViewset
from .filters import (
    UnitFilter, PremisesFilter, RentPaymentFilter, RentAccountFilter
)


from clients.models import Client


class PremisesViewSet(
    viewsets.ModelViewSet, AbstractBaseFilterViewset, APIView,
):
    """Premises API endpoint."""

    def create(self, request):
        """Override default create."""
        user = request.user
        owner = Client.objects.get(user=user)
        serializer = PremisesSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            location = serializer.validated_data.get('location')
            premises_type = serializer.validated_data.get('premises_type')
            building_type = serializer.validated_data.get('building_type')

            premises = Premises.objects.create(
                owner=owner,
                name=name,
                location=location,
                premises_type=premises_type,
                building_type=building_type
            )

            return Response(
                status=status.HTTP_201_CREATED,
                # data=premises
            )

    def get_queryset(self):
        """Get premises belonging to the logged in user."""
        user = self.request.user
        owner = Client.objects.get(user=user)
        premises = Premises.objects.filter(owner=owner)
        return premises

    serializer_class = PremisesSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_class = PremisesFilter


class UnitViewSet(viewsets.ModelViewSet, AbstractBaseFilterViewset, APIView):
    """API endpoint for managing premises units."""

    def get_queryset(self):
        """Get units belonging to premises owned by the user."""
        user = self.request.user
        owner = Client.objects.get(user=user)
        units = Unit.objects.filter(premises__owner=owner)
        return units

    serializer_class = UnitSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_class = UnitFilter


class RentPaymentViewSet(
    viewsets.ModelViewSet, AbstractBaseFilterViewset, APIView
):
    """Api endpoint for managing rental payments."""

    def get_queryset(self):
        """Get rent paymentd for units in premises owner by the user."""
        user = self.request.user
        owner = Client.objects.get(user=user)
        rent_payments = RentPayment.objects.filter(
            unit__premises__owner=owner
        )
        return rent_payments

    serializer_class = RentPaymentSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_class = RentPaymentFilter


class RentAccountViewSet(
    viewsets.ModelViewSet, AbstractBaseFilterViewset, APIView
):
    """Api endpoint for managing rent accounts."""

    def get_queryset(self):
        """."""
        user = self.request.user
        owner = Client.objects.get(user=user)
        rent_accounts = RentAccount.objects.filter(
            premises__owner=owner
        )
        return rent_accounts

    serializer_class = RentAccountSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_class = RentAccountFilter


def index(request):
    """Rental Houses Index Page."""
    return render(
        request, "rental_houses/index.html",
    )


@ login_required
def my_premises(request):
    """List the premises a client owns."""
    user = get_user(request)
    owner = Client.objects.get(user=user)
    my_premises = Premises.objects.filter(owner=owner)

    context = {
        "my_premises": my_premises,
    }
    return render(
        request, "rental_houses/my_property.html", context
    )


@ login_required
def add_premises(request):
    """Add appartment View.

    TODO rename this view.
    """
    if request.method == "POST":
        form = PremisesForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            location = form.cleaned_data['location']
            premises_type = form.cleaned_data['premises_type']
            building_type = form.cleaned_data['building_type']

            user = get_user(request)
            owner = Client.objects.get(user=user)

            Premises.objects.create(
                owner=owner,
                name=name,
                location=location,
                premises_type=premises_type,
                building_type=building_type,
            )
            # redirect('rental_houses:view_premises', )
            return redirect('rental_houses:my_property')
            # return HttpResponse(f"Dear {owner} Property added successfully")
    else:
        form = PremisesForm()
    context = {
        'form': form
    }
    return render(
        request, 'rental_houses/add_appartment.html', context
    )


@ login_required
def view_premises(request, premises_id):
    """View a single premises."""
    user = get_user(request)
    owner = Client.objects.get(user=user)
    premises = Premises.objects.get(id=premises_id, owner=owner)
    available_houses = Unit.objects.filter(premises=premises)

    context = {
        'premises': premises,
        'no_of_houses': available_houses.count(),
        'available_houses': available_houses,
    }
    return render(request, 'rental_houses/view_premises.html', context)


@ login_required
def add_house_to_premises(request, premises_id):
    """Add house to a premises."""
    user = get_user(request)
    owner = Client.objects.get(user=user)
    premises = Premises.objects.get(id=premises_id, owner=owner)
    available_houses = Unit.objects.filter(premises=premises)
    if request.method == "POST":
        form = UnitForm(request.POST)
        if form.is_valid():
            unit_number = form.cleaned_data['unit_number']
            unit_type = form.cleaned_data['unit_type']
            rent = form.cleaned_data['rent']
            tenant_id_no = form.cleaned_data['tenant_id_no']
            tenant_name = form.cleaned_data['tenant_name']
            tenant_phone_number = form.cleaned_data['tenant_phone_number']

            Unit.objects.create(
                premises=premises,
                unit_number=unit_number,
                unit_type=unit_type,
                rent=rent,
                tenant_id_no=tenant_id_no,
                tenant_name=tenant_name,
                tenant_phone_number=tenant_phone_number,
            )
            # return redirect('rental_houses:premises_houses_list)
            return redirect('rental_houses:add_house', premises.id)
    else:
        form = UnitForm()
    context = {
        'form': form,
        'premises': premises,
        'available_houses': available_houses,
    }
    return render(request, "rental_houses/add_house.html", context)


@ login_required
def view_premises_units(request, premises_id):
    """View houses in a certain premises."""
    user = get_user(request)
    owner = Client.objects.get(user=user)
    premises = Premises.objects.get(id=premises_id, owner=owner)
    available_units = Unit.objects.filter(premises=premises)

    context = {
        'available_units': available_units,
        'premises': premises
    }
    return render(
        request, 'rental_houses/view_premises_houses.html', context
    )


@ login_required
def view_single_unit(request, premises_id, unit_id):
    """."""
    user = get_user(request)
    owner = Client.objects.get(user=user)
    premises = Premises.objects.get(id=premises_id, owner=owner)
    unit = Unit.objects.get(id=unit_id, premises=premises)
    context = {
        'unit': unit,
        'premises': premises,
    }
    return render(
        request, 'rental_houses/view_single_unit.html', context
    )


@ login_required
def add_rent_payment(request, premises_id, unit_id):
    """Record a rental payment."""
    user = get_user(request)
    owner = Client.objects.get(user=user)
    premises = Premises.objects.get(id=premises_id, owner=owner)
    unit = Unit.objects.get(id=unit_id, premises=premises)

    if request.method == "POST":
        form = RentPaymentForm(request.POST)
        if form.is_valid():
            # unit_number = form.cleaned_data['unit_number']
            month = form.cleaned_data['month']
            year = form.cleaned_data['year']
            currency = form.cleaned_data['currency']
            payment_method = form.cleaned_data['payment_method']
            amount_paid = form.cleaned_data['amount_paid']
            date_paid = form.cleaned_data['date_paid']
            transaction_id = form.cleaned_data['transaction_id']
            payer_name = form.cleaned_data['payer_name']
            payer_phone_no = form.cleaned_data['payer_phone_no']

            RentPayment.objects.create(
                unit=unit,
                month=month,
                year=year,
                currency=currency,
                payment_method=payment_method,
                amount_paid=amount_paid,
                date_paid=date_paid,
                transaction_id=transaction_id,
                payer_name=payer_name,
                payer_phone_no=payer_phone_no,
            )

            return HttpResponse(
                """Payment successfull
                {} {} {} {} {} {} {} {} {}
                """.format(
                    unit, month, year, currency, payment_method, amount_paid,
                    date_paid, payer_name, payer_phone_no
                )
            )
    else:
        form = RentPaymentForm()
    context = {
        'form': form
    }
    return render(
        request, 'rental_houses/add_rent_payment.html', context
    )
