from django.contrib import admin

from .models import (
    # Client,
    Premises,
    Unit,
    RentPayment,
)


class PremisesAdmin(admin.ModelAdmin):
    """Premises Admin model."""

    list_display = (
        'owner', 'name', 'location', 'building_type', 'premises_type'
    )
    search_fields = ['owner', 'name', 'location']
    list_filter = ['building_type']


# admin.site.register(Client, ClientAdmin)


class UnitAdmin(admin.ModelAdmin):
    """."""

    list_display = (
        'premises', 'unit_number', 'unit_type', 'rent',
        'tenant_name', 'tenant_phone_number',
    )
    search_fields = ['premises__name']


class RentPaymentAdmin(admin.ModelAdmin):
    """."""

    list_display = (
        'unit', 'month', 'year', 'date_paid', 'payer_name',
        'month_year',
    )


admin.site.register(Premises, PremisesAdmin)
admin.site.register(Unit, UnitAdmin)
admin.site.register(RentPayment, RentPaymentAdmin)
