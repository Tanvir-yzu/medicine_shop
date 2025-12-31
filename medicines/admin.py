# medicines/admin.py
from django.contrib import admin
from .models import Medicine, ScanLog
from django.utils import timezone

# Custom Action for Medicine Admin
def mark_as_out_of_stock(modeladmin, request, queryset):
    """Bulk action to set the stock of selected medicines to 0."""
    queryset.update(stock=0)
mark_as_out_of_stock.short_description = "Mark selected medicines as Out of Stock"

@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    """Custom admin interface for the Medicine model."""

    # Fields to display in the list view
    list_display = (
        'name',
        'batch_number',
        'manufacturer',
        'expiry_date',
        'stock_status',  # Custom method to display stock with color
        'price',
        'created_at',
    )

    # Fields that can be searched
    search_fields = ('name', 'batch_number', 'manufacturer', 'generic_name')

    # Fields to filter by in the sidebar
    list_filter = (
        'manufacturer',
        ('expiry_date', admin.DateFieldListFilter), # Filter by date
    )

    # Fields that are read-only and cannot be edited
    readonly_fields = ('qr_code', 'created_at', 'updated_at')

    # Custom actions available in the list view
    actions = [mark_as_out_of_stock]

    # Organize fields into tabs/sections for better readability in the edit form
    fieldsets = (
        ('Medicine Information', {
            'fields': ('name', 'generic_name', 'manufacturer', 'batch_number', 'description')
        }),
        ('Inventory & Pricing', {
            'fields': ('expiry_date', 'price', 'stock')
        }),
        ('System Generated', {
            'fields': ('qr_code', 'created_at', 'updated_at'),
            'classes': ('collapse',), # Makes this section collapsible
        }),
    )

    def stock_status(self, obj):
        """Custom method to display stock with a colored badge."""
        if obj.stock <= 0:
            return f'<span style="color: white; background-color: #dc2626; padding: 2px 8px; border-radius: 12px;">Out of Stock</span>'
        elif obj.stock < 5:
            return f'<span style="color: white; background-color: #f59e0b; padding: 2px 8px; border-radius: 12px;">Low Stock</span>'
        else:
            return f'<span style="color: white; background-color: #10b981; padding: 2px 8px; border-radius: 12px;">In Stock</span>'
    
    # Allow HTML in the stock_status display
    stock_status.allow_tags = True
    # Set a user-friendly name for the column
    stock_status.short_description = 'Stock Status'

    def get_queryset(self, request):
        """Override queryset to add expiry date highlighting."""
        qs = super().get_queryset(request)
        # You could annotate or process the queryset here if needed
        return qs


@admin.register(ScanLog)
class ScanLogAdmin(admin.ModelAdmin):
    """Custom admin interface for the ScanLog model."""

    # Fields to display in the list view
    list_display = (
        'id',
        'user',
        'recognized',
        'medicine_link', # Custom method to link to the medicine
        'scanned_data_truncated', # Truncate long data for better display
        'timestamp',
    )

    # Fields that can be searched
    search_fields = ('scanned_data', 'user__username', 'medicine__name', 'medicine__batch_number')

    # Fields to filter by in the sidebar
    list_filter = (
        'recognized',
        'user',
        ('timestamp', admin.DateFieldListFilter),
    )

    # Make all fields read-only, as logs should not be modified
    readonly_fields = [field.name for field in ScanLog._meta.get_fields()]
    
    # Disable the 'Add' button since logs are created programmatically
    def has_add_permission(self, request):
        return False

    # Disable the 'Delete' action
    def has_delete_permission(self, request, obj=None):
        return False
        
    def medicine_link(self, obj):
        """Display a link to the related medicine if it was recognized."""
        if obj.medicine:
            return f'<a href="/admin/medicines/medicine/{obj.medicine.id}/change/">{obj.medicine.name} ({obj.medicine.batch_number})</a>'
        return '-'
    medicine_link.allow_tags = True
    medicine_link.short_description = 'Medicine'

    def scanned_data_truncated(self, obj):
        """Truncate the scanned data for better display in the list view."""
        max_length = 50
        if len(obj.scanned_data) > max_length:
            return f"{obj.scanned_data[:max_length]}..."
        return obj.scanned_data
    scanned_data_truncated.short_description = 'Scanned Data'