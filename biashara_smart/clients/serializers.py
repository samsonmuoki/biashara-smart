from rest_framework import serializers
from .models import Client


class ClientSerializer(serializers.ModelSerializer):
    """Serialize clients who own businesses."""

    class Meta:
        """."""

        model = Client
        fileds = '__all__'


class OwnerSerializer(serializers.ModelSerializer):
    """Get the client User instance of the user making the request."""

    class Meta:
        """."""

        model = Client
        fields = '__all__'
