from rest_framework import viewsets, decorators, response
from rest_framework.exceptions import NotFound
from rest_framework.response import Response

from invoices.models import Invoice
from invoices.serializers import InvoiceSerializer


class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

    @decorators.action(detail=True, methods=['post', 'get'])
    def pay(self, request, pk=None):
        if request.method == 'GET':
            invoice = self.get_object()
            invoice.paid = True
            invoice.save()
            return response.Response({'status': 'paid' if invoice.paid else 'unpaid'})

        # TODO 5: Completar la vista para marcar la factura como pagada
        # Si la factura ya está pagada, devolver un error con status 400
        if request.method == 'POST':
            invoice = self.get_object()
            if invoice.paid:
                raise NotFound(detail="Esa factura ya estaba paga")
            else:
                invoice.paid = True
                invoice.save()
                return response.Response({'status': 'paid'})

    @decorators.action(detail=True, methods=['get'])
    def subtotal(self, request, pk=None):
        invoice = self.get_object()
        subtotal = invoice.subtotal()
        return Response({'subtotal': subtotal})  # Devuelve el resultado    @decorators.action(detail=True, methods=['get'])

    @decorators.action(detail=True, methods=['get'])
    def total(self, request, pk=None):
        invoice = self.get_object()
        total = invoice.total()
        return Response({'total': total})  # Devuelve el resultado
