from django.utils import timezone
from rest_framework import viewsets, decorators, response, status
from invoices.models import Invoice
from invoices.serializers import InvoiceSerializer


class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    
    @decorators.action(detail=True, methods=['post', 'get'])
    def pay(self, request, pk=None):
        if request.method == 'GET':
            invoice = self.get_object()
            return response.Response({'status': 'paid' if invoice.paid else 'unpaid'})
        
        # if request.method == 'POST':
            # TODO 5: Completar la vista para marcar la factura como pagada
            # Si la factura ya está pagada, devolver un error con status 400
        if request.method == 'POST':
            invoice = self.get_object()
            if invoice.paid:
                return response.Response(
                    {'error': 'La factura ya está pagada.'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            # Marcar la factura como pagada
            invoice.paid = True
            invoice.payment_date = timezone.now()
            invoice.save()
            return response.Response({'status': 'Factura marcada como pagada.'}, status=status.HTTP_200_OK)
