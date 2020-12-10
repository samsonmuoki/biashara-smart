from django_filters import rest_framework as filters
from rest_framework import generics


class AbstractBaseFilterViewset(generics.ListAPIView):
    """Base class to be used by most viewsets when filtering."""
    filter_backends = (filters.DjangoFilterBackend,)
