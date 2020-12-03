from rest_framework import serializers
from .models import Premises


class PremisesSerializer(serializers.ModelSerializer):
    """Premises serializer."""
    class Meta:
        """."""
        model = Premises
        fields = "__all__"
