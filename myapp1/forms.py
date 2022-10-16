from django import forms
from myapp1.models import OrderItem

class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['item', 'client', 'items_ordered']
        widgets = {
            'client': forms.RadioSelect(),
        }
        labels = {
            'items_ordered': 'Quantity',
            'client': 'Client Name',
        }

class InterestForm(forms.Form):
    CHOICES = [(1, 'Yes'), (0, 'No')]
    interested = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    quantity = forms.IntegerField(initial=1)
    comments = forms.CharField(widget=forms.Textarea)
    class Meta:
        labels = {
            'comments': 'Additional Comments',
        }