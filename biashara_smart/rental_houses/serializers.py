from rest_framework import serializers
from .models import Premises, Unit, RentPayment, ExpensePayment


class PremisesSerializer(serializers.ModelSerializer):
    """Premises serializer."""
    class Meta:
        """."""
        model = Premises
        fields = "__all__"


class UnitSerializer(serializers.ModelSerializer):
    """."""

    class Meta:
        """."""
        model = Unit
        fields = "__all__"


class RentPaymentSerializer(serializers.ModelSerializer):
    """."""

    class Meta:
        """."""
        model = RentPayment
        fields = "__all__"


class ExpensePaymentSerializer(serializers.ModelSerializer):
    """."""

    class Meta:
        """."""
        model = ExpensePayment
        fields = "__all__"
