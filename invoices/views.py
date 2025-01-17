from rest_framework import viewsets, decorators, response
from invoices.models import Invoice
from invoices.serializers import InvoiceSerializer
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK


class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    
    @decorators.action(detail=True, methods=['post', 'get'])
    def pay(self, request, pk=None):
        if request.method == 'GET':
            invoice = self.get_object()
            return response.Response({'status': 'paid' if invoice.paid else 'unpaid'})
        
        if request.method == 'POST':
            # TODO 5: Completar la vista para marcar la factura como pagada
            # Si la factura ya está pagada, devolver un error con status 400
        
            invoice = self.get_object()
            if invoice.paid:
                return response.Response(
                    {'error': 'Invoice already paid'}, status=HTTP_400_BAD_REQUEST
                )
            invoice.paid = True
            invoice.save()

            return response.Response({'status': 'Invoice marked as paid'}, status=HTTP_200_OK)