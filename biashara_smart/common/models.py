import uuid
from django.db import models


class AbstractBase(models.Model):
    """Base class for most models in the project."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    created_by = models.UUIDField(blank=True, null=True)
    updated_by = models.UUIDField(blank=True, null=True)

    class Meta:
        """Metadata options."""
        abstract = True


class Person(AbstractBase, models.Model):
    """Abstract person."""

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=50)
    national_id = models.IntegerField(null=True, blank=True)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField(max_length=50, null=False, blank=True)

    class Meta:
        """Meta options."""

        abstract = True


class Business(AbstractBase, models.Model):
    """Abstract Business Model."""

    name_of_business = models.CharField(max_length=100)
    email_address = models.EmailField(max_length=100, null=True, blank=True)
    physical_address = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        """Metadata options."""

        abstract = True
