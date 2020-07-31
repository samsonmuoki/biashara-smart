from django.contrib import admin

from . models import Client


class ClientAdmin(admin.ModelAdmin):
    """Client admin model."""

    list_display = (
        'phone_number', 'first_name', 'last_name', 'email',
        'created', 'updated',
    )
    search_fields = ['first_name', 'last_name', 'phone_number', 'email']
    # list_filter = []


admin.site.register(Client, ClientAdmin)
