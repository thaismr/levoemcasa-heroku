from django.contrib import admin
from . models import Product, Variation


class VariationInline(admin.TabularInline):
    model = Variation
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'summary', 'get_price_from', 'price_sale']
    inlines = [
        VariationInline,
    ]


# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Variation)
