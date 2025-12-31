from django.contrib import admin
from django.utils.html import format_html
from .models import Medicine, ScanLog


@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'batch_number',
        'manufacturer',
        'expiry_date',
        'price',
        'stock',
        'qr_code_image',
    )

    search_fields = (
        'name',
        'generic_name',
        'batch_number',
    )

    list_filter = (
        'manufacturer',
        'expiry_date',
    )

    readonly_fields = (
        'qr_code_image',
        'created_at',
        'updated_at',
    )

    fieldsets = (
        ('Medicine Information', {
            'fields': (
                'name',
                'generic_name',
                'manufacturer',
                'batch_number',
                'description',
            )
        }),
        ('Stock & Pricing', {
            'fields': (
                'price',
                'stock',
                'expiry_date',
            )
        }),
        ('QR Code', {
            'fields': (
                'qr_code_image',
            )
        }),
        ('Timestamps', {
            'fields': (
                'created_at',
                'updated_at',
            )
        }),
    )

    def qr_code_image(self, obj):
        if obj.qr_code:
            return format_html(
                '<img src="{}" width="120" height="120" />',
                obj.qr_code.url
            )
        return "No QR Code"

    qr_code_image.short_description = "QR Code"


@admin.register(ScanLog)
class ScanLogAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'medicine',
        'recognized',
        'timestamp',
    )

    list_filter = (
        'recognized',
        'timestamp',
    )

    search_fields = (
        'scanned_data',
        'user__username',
    )

    readonly_fields = (
        'scanned_data',
        'medicine',
        'recognized',
        'timestamp',
        'user',
    )
