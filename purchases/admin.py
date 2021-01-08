from django.contrib import admin
from .models import Purchase, PurchaseItem


# Add inline form to include 'purchase item'
class PurchaseItemInline(admin.TabularInline):
    model = PurchaseItem
    extra = 1


# Show inline form at 'Purchase' admin
class PurchaseAdmin(admin.ModelAdmin):
    inlines = [
        PurchaseItemInline,
    ]


# Register your models here.
admin.site.register(Purchase, PurchaseAdmin)
admin.site.register(PurchaseItem)
