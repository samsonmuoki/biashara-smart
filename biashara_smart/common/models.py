import uuid
from django.db import models


class Person(models.Model):
    """Abstract person."""

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    first_name = models.CharField(max_length=20)
    other_names = models.CharField(max_length=50)
    national_id = models.IntegerField(null=False)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField(max_length=50, null=False, blank=True)

    class Meta:
        """Meta options."""

        abstract = True


class Business(models.Model):
    """Abstract Business Model."""

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    name_of_business = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    class Meta:
        """Metadata options."""

        abstract = True
