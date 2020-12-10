from rest_framework import serializers
from .models import Premises, Unit, RentPayment, ExpensePayment, RentAccount


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

    def create(self, validated_data):
        """Override create method to track rental payments."""
        amount_paid = validated_data.get('amount_paid')
        unit = validated_data.get('unit')
        tenant_id_no = unit.tenant_id_no
        premises = unit.premises
        account_name = unit.tenant_name

        rent_account, _ = RentAccount.objects.get_or_create(
            tenant_id_no=tenant_id_no,
            premises=premises,
            defaults={
                'account_name': account_name
            }
        )
        amount = rent_account.amount
        new_amount = float(amount) + float(amount_paid)
        rent_account.amount = new_amount
        rent_account.save()

        rent_payment = RentPayment.objects.create(
            unit=validated_data['unit'],
            month=validated_data['month'],
            year=validated_data['year'],
            payer_name=validated_data['payer_name'],
            payer_phone_no=validated_data['payer_phone_no'],
            payer_national_id=validated_data['payer_national_id'],
            date_paid=validated_data['date_paid'],
            currency=validated_data['currency'],
            amount_paid=validated_data['amount_paid'],
            payment_method=validated_data['payment_method'],
        )
        return rent_payment


class RentAccountSerializer(serializers.ModelSerializer):
    """Serializer for rent payemnt accounts."""

    class Meta:
        """."""
        model = RentAccount
        fields = "__all__"


class ExpensePaymentSerializer(serializers.ModelSerializer):
    """."""

    class Meta:
        """."""
        model = ExpensePayment
        fields = "__all__"
