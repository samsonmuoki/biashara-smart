from django.forms import ModelForm
from django import forms
from .models import Premises, Unit, RentPayment
from common.constants import (
    CURRENCY_CHOICES, PAYMENT_METHODS,  # YEAR_CHOICES
)


class PremisesForm(ModelForm):
    """Add a Premises Form."""

    class Meta:
        """Form fields."""
        model = Premises
        fields = [
            'name', "location", "premises_type", "building_type"
        ]


class UnitForm(ModelForm):
    """Add a house/unit form."""

    class Meta:
        """Form fields."""
        model = Unit
        fields = [
            'unit_number', 'unit_type', 'rent',
            'tenant_id_no', 'tenant_name', 'tenant_phone_number'
        ]


class RentPaymentForm(ModelForm):
    """Record a rent payment."""

    class Meta:
        """Form fields."""
        model = RentPayment
        fields = [
            'month', 'year', 'currency', 'payment_method', 'amount_paid',
            'transaction_id', 'date_paid', 'payer_name', 'payer_phone_no',
        ]
