from cProfile import label
from fileinput import FileInput
from django.forms import ModelForm
from django import forms
from .models import Order, Detalle

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        labels = {
            'provider': 'proveedor',
            'ordernumber': 'numero de orden',
            'orderdate': 'fecha de orden',
            'senddate': 'fecha de envio',
        }

        widgets = {
            'provider': forms.TextInput(),
            'ordernumber': forms.NumberInput(),
            'orderdate': forms.DateInput(attrs={'type': 'date'}),
            'senddate': forms.DateInput(attrs={'type': 'date'}),
        }

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

class DetalleForm(ModelForm):
    class Meta:
        model = Detalle
        fields = '__all__'
        labels = {
            'order': 'orden',
            'product': 'producto',
            'filedetalle': 'detalle del archivo',
            'cantidad': 'cantidad',
            'monto': 'monto',
        }

        widgets = {
            'order': forms.TextInput(),
            'product': forms.TextInput(),
            'filedetalle': forms.FileInput(),
            'cantidad': forms.NumberInput(),
            'monto': forms.NumberInput(),
        }

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)