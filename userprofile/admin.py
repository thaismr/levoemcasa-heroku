from django.contrib import admin
from .models import UserProfile, UserAddress


class UserAddressInline(admin.StackedInline):
    model = UserAddress
    extra = 1


class UserProfileAdmin(admin.ModelAdmin):
    inlines = [
        UserAddressInline,
    ]


# Register your models here.
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(UserAddress)
