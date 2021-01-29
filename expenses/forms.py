from django import forms
from .models import Expense

class ExpenseModelForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'})
        }
        labels = {
            'name': '花費項目',
            'price': '金額'
        }