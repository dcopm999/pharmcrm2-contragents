# -*- coding: utf-8 -*-
from django.contrib import admin

from contragents import models


class ContactInline(admin.StackedInline):
    model = models.Contact
    suit_classes = "suit-tab suit-tab-contact"
    extra = 1


@admin.register(models.Contragent)
class ContragentAdmin(admin.ModelAdmin):
    inlines = [ContactInline]
    search_fields = ["name"]
    autocomplete_fields = ["manager"]
    suit_form_tabs = (
        ("general", "General"),
        ("address", "Address"),
        ("contact", "Contact"),
    )

    fieldsets = [
        (
            "General",
            {
                "classes": (
                    "suit-tab",
                    "suit-tab-general",
                ),
                "fields": ["contragent_type", "name", "manager"],
            },
        ),
        (
            None,
            {
                "classes": (
                    "suit-tab",
                    "suit-tab-general",
                ),
                "fields": ["inn", "okonh", "okpo", "oked"],
            },
        ),
        (
            "Address",
            {
                "classes": (
                    "suit-tab",
                    "suit-tab-address",
                ),
                "fields": [
                    "country",
                    "region",
                    "city",
                    "district",
                    "street",
                    "address_ur",
                ],
            },
        ),
    ]
