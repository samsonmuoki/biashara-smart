# import django_filters
from django_filters import rest_framework as filters

from .models import (
    Premises, Unit, RentPayment, ExpensePayment, RentAccount
)


class PremisesFilter(filters.FilterSet):
    """Filters for premises."""

    class Meta:
        """."""
        model = Premises
        fields = ['location', 'premises_type', 'building_type']


class UnitFilter(filters.FilterSet):
    """Filter units by premises."""

    class Meta:
        """."""
        model = Unit
        fields = ['premises']


class RentPaymentFilter(filters.FilterSet):
    """Filters for rent payments."""

    class Meta:
        """."""

        model = RentPayment
        fields = [
            'unit', 'month', 'year', 'payer_name', 'payer_phone_no',
            'payer_national_id', 'payment_method', 'date_paid'
        ]


class RentAccountFilter(filters.FilterSet):
    """Filters for rent accounts."""

    class Meta:
        """."""

        model = RentAccount
        fields = ['premises', 'account_name', 'tenant_id_no']


class ExpensePaymentFilter(filters.FilterSet):
    """Filters for expense payments."""

    class Meta:
        """."""

        model = ExpensePayment
        fields = ['name', 'premises', 'expense_type', 'provider']
