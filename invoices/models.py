from django.db import models
from django.db.models import Sum
from django.core.validators import MinValueValidator, MaxValueValidator
from decimal import Decimal


class Invoice(models.Model):
    number = models.CharField(max_length=10)
    date = models.DateField()
    customer = models.CharField(max_length=100)
    paid = models.BooleanField(default=False)
    payment_date = models.DateField(null=True, blank=True)
    
    # TODO 1: Implementar el método total usando una expresión de agregación 
    # https://docs.djangoproject.com/en/5.1/topics/db/aggregation/
    def subtotal(self):
        return self.items.aggregate(total=Sum('price'))['total'] or 0 # Linea de Breynner Sierra.
    
    # TODO 2: Implementar el método total usando la función sum() y una lista por comprensión
    # Se debe multiplicar el valor del item por 1.19 sólo si la cantidad es mayor a 2
    def total(self):
        return sum(float(item.price) * 1.19 if item.quantity > 2 else float(item.price) for item in self.items.all()) # Linea de Breynner Sierra.

class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='items')
    description = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    # TODO 3: Implementar un campo retención en la fuente "withholding" con un valor por defecto de 0, 
    # que puede recibir valores con dos decimales entre 0 y 10 con un paso de 0.01
    # Implementarlo con un validador de rango

    withholding = models.DecimalField( # Linea de Breynner Sierra
        max_digits=4,
        decimal_places=2,
        default=Decimal('0.00'),
        validators=[
            MinValueValidator(Decimal('0.00')),  
            MaxValueValidator(Decimal('10.00'))  
        ]
    )
    
    def unit_price(self):
        return self.price/self.quantity
    
    def __str__(self):
        return self.description
    
