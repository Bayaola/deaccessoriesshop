from decimal import Decimal
from unicodedata import name

from django.conf import settings
from django.db import models
from Stores.models import Product
from .utils import PAYMENT_CHOICES


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="order_user")
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20, null=True, blank=True)
    country_code = models.CharField(max_length=4, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    total_paid = models.DecimalField(max_digits=5, decimal_places=2)
    payment_option = models.ForeignKey('PayementMethode', on_delete=models.RESTRICT, related_name="payment_option", default='')
    id_trasaction = models.CharField(max_length=200)
    billing_status = models.BooleanField(default=False)

    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return str(self.created)


class PayementMethode(models.Model):
    name = models.CharField(choices=PAYMENT_CHOICES, max_length=150, unique=True)
    name_of_the_beneficiary = models.CharField(max_length=250, null=True)
    number_id = models.CharField(max_length=150, unique=True, null=True)
    image = models.ImageField(upload_to="images/qr_code/", blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.name in ('USDT (TETHER)', 'BITCOIN (BTC)'):
            if not self.image:
                from tempfile import TemporaryFile
                from django.core.files.storage import default_storage
                from django.core.files.base import ContentFile
                from django.utils.encoding import force_str
                import qrcode
                with TemporaryFile() as f:
                    img = qrcode.make(self.number_id)
                    img.save(f)
                    f.seek(0)
                    self.image = default_storage.save(force_str("%s.png"%self.name), ContentFile(f.read()))
        super(PayementMethode, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.name)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="order_items", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)