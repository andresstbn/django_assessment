from rest_framework import serializers
from invoices.models import Invoice, InvoiceItem


class InvoiceItemSerializer(serializers.ModelSerializer):

    # TODO 4: Descomentar esta línea y resolver el error
    #unit_price = serializers.ReadOnlyField()
    unit_price = serializers.SerializerMethodField()

    class Meta:
        model = InvoiceItem
        fields = "__all__"

    def get_unit_price(self, obj):
        return obj.price * (1 - (obj.withholding / 100))

class InvoiceSerializer(serializers.ModelSerializer):
    items = InvoiceItemSerializer(many=True)
    subtotal = serializers.ReadOnlyField()
    total = serializers.ReadOnlyField()
    
    class Meta:
        model = Invoice
        fields = "__all__"

