from rest_framework import serializers
from .models import Client


class ClientSerializer(serializers.ModelSerializer):
    """Serialize clients who own businesses."""

    class Meta:
        """."""

        model = Client
        fileds = '__all__'
