from rest_framework import serializers
from invoices.models import Invoice, InvoiceItem


class InvoiceItemSerializer(serializers.ModelSerializer):
    
    # TODO 4: Descomentar esta línea y resolver el error
    unit_price = serializers.SerializerMethodField() # Linea de Breynner Sierra
    

    def get_unit_price(self, obj): # Linea de Breynner Sierra
        return obj.unit_price()  
    

    class Meta:
        model = InvoiceItem
        fields = "__all__"

class InvoiceSerializer(serializers.ModelSerializer):
    items = InvoiceItemSerializer(many=True)
    subtotal = serializers.ReadOnlyField()
    total = serializers.ReadOnlyField()
    
    class Meta:
        model = Invoice
        fields = "__all__"

