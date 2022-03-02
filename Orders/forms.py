from django import forms
from django.forms import ModelForm
from .models import Order
# from .utils import PAYMENT_CHOICES

# class PayementForm(forms.Form):
#     address = forms.CharField(max_length=250)
#     city = forms.CharField(max_length=100)
#     postal_code = forms.CharField(max_length=20)
#     country_code = forms.CharField(max_length=4)
#     total_paid = forms.DecimalField(max_digits=5, decimal_places=2)
#     payment_option = forms.ChoiceField(choices=PAYMENT_CHOICES, required=True)
#     order_key = forms.CharField(max_length=200)

class PayementForm(ModelForm):
    class Meta:
        model = Order
        fields = ['address', 'city', 'postal_code', 'country_code', 'total_paid', 'payment_option', 'order_key']
