from django import forms
from apps.stock.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['disponibility','store']
        labels = {
            'name': 'Nome do Produto',
            'price': 'Preço do Produto',
            'description': 'Breve descrição sobre o produto',
            'quantity': 'Quantidade do produto em stock',
            'disponibility': 'Disponibilidade do Produto',
            'stockDate':'Data de compra do produto',
            'productPhoto':'Foto do produto, caso tenha',
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'stockDate': forms.DateTimeInput(format='%d/%m/%Y',
                                         attrs={'class': 'form-control', 'type': 'date',}),
            'productPhoto': forms.FileInput(attrs={'class': 'form-control'}),
    }

