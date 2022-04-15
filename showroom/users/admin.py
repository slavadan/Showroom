from django.contrib import admin
from .models import ShowroomUser


@admin.register(ShowroomUser)
class ShowroomUserAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'date_joined',
        'is_supplier',
        'is_customer',
        'is_showroom',
    )
    list_filter = (
        'is_supplier',
        'date_joined',
    )
    readonly_fields = ['date_joined']
