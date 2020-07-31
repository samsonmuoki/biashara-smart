import datetime
from django.db import models
# from django.contrib.auth.models import User

from common.models import AbstractBase
from common.constants import (
    MONTH_CHOICES, YEAR_CHOICES, CURRENCY_CHOICES, PAYMENT_METHODS,
    EXPENSE_TYPES
)
from clients.models import Client


PREMISES_TYPES = (
    ("residential", "Residential eg family houses, bedsitters"),
    ("educational", "Educational eg schools, colleges"),
    ("institutional", "Institutional eg churches, hospitals"),
    ("business", "Business eg offices, banks, courthouses"),
    ("mercantile", "Mercantile eg shops, stores, showrooms"),
    ("industrial", "Industrial eg assembly plants, manufacturing"),
)


BUILDING_TYPES = (
    ('storey', "Storey"),
    ("bungalow", "Bungalow"),
    ("other", "Other"),
)

UNIT_TYPES = (
    ("cube", "Cube"),
    ('bedsitter', "Bedsitter"),
    ("one_bedroom", "One Bedroom"),
    ("two_bedroom", "Two Bedroom"),
    ("three_bedroom", "Three Bedroom"),
    ("four_bedroom", "Four Bedroom"),
    ("five_bedroom", "Five Bedroom"),
    ("shop", "Shops"),  # TODO better representation of shops
)


class Premises(AbstractBase, models.Model):
    """A house or building owned by a client.
    Includes its land and outbuildings.
    """

    owner = models.ForeignKey(Client, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    premises_type = models.CharField(
        max_length=20, choices=PREMISES_TYPES
    )
    building_type = models.CharField(
        max_length=20, choices=BUILDING_TYPES
    )

    def __str__(self):
        """String to represent a premises."""
        return f"{self.name} -- {self.owner}"


class Unit(AbstractBase, models.Model):
    """A single house/unit for rent."""

    premises = models.ForeignKey(
        Premises, on_delete=models.PROTECT, blank=True, null=True
    )
    unit_number = models.CharField(max_length=50)
    unit_type = models.CharField(
        max_length=50, choices=UNIT_TYPES
    )
    rent = models.DecimalField(
        max_digits=19, decimal_places=2
    )
    # TODO utilities = water, electricity, dstv, etc
    # TENANTS DETAILS
    tenant_id_no = models.IntegerField(null=True, blank=True)
    tenant_name = models.CharField(max_length=100, null=True, blank=True)
    tenant_phone_number = models.CharField(
        max_length=15, null=True, blank=True
    )
    tenant_email = models.EmailField(max_length=250)

    class Meta:
        """Meta options."""
        unique_together = ['premises', 'unit_number']

    def __str__(self):
        """Represent a house unit."""
        return f"{self.premises} -- {self.unit_number}, Rent: {self.rent}"


class RentPayment(AbstractBase, models.Model):
    """Rent Payment."""

    # building = models.ForeignKey(Building, on_delete=models.PROTECT)
    unit = models.ForeignKey(Unit, on_delete=models.PROTECT)
    month = models.PositiveIntegerField(
        default=1, choices=MONTH_CHOICES, null=True
    )
    year = models.PositiveIntegerField(
        default=2020, null=True, choices=YEAR_CHOICES
    )
    payer_name = models.CharField(max_length=100, null=True, blank=True)
    payer_phone_no = models.CharField(max_length=100, null=True, blank=True)
    payer_national_id = models.CharField(max_length=20, null=True, blank=True)
    date_paid = models.DateField(auto_now_add=False, auto_now=False)
    currency = models.CharField(max_length=10, choices=CURRENCY_CHOICES)
    amount_paid = models.DecimalField(max_digits=19, decimal_places=2)
    payment_method = models.CharField(
        max_length=20, choices=PAYMENT_METHODS, null=False, blank=False
    )
    transaction_id = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        """Represent a rent payment."""
        return f"{self.house}: {self.amount_paid} -> {self.date_paid}"

    def month_year(self):
        """Return a datetime object for the payment using month and year."""
        rent_date_string = "1/{}/{}".format(self.month, self.year)
        return datetime.datetime.strptime(rent_date_string, "%d/%m/%Y").date()


class ExpensePayment(AbstractBase, models.Model):
    """Expenses incurred from operating the business."""

    name = models.CharField(max_length=50, null=False, blank=False)
    premises = models.ForeignKey(Premises, on_delete=models.CASCADE)
    expense_type = models.CharField(
        max_length=20, choices=EXPENSE_TYPES, null=False
    )
    provider = models.CharField(max_length=50, null=True)
    date_paid = models.DateField(auto_now_add=True, null=True)
