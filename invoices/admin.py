from django.contrib import admin
from invoices.models import Invoice, InvoiceItem


admin.site.site_header = "Datak Assessment"
admin.site.site_title = "Datak Assessment"
admin.site.index_title = "Welcome to Datak Assessment"


class InvoiceItemInline(admin.TabularInline):
    model = InvoiceItem


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    inlines = [InvoiceItemInline]
    list_display = ('number', 'date', 'customer', 'paid', 'payment_date')
    list_filter = ('paid',)
    search_fields = ('number', 'customer')
