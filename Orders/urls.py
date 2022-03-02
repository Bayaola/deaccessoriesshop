from django.urls import path
from .views import *

app_name = 'Orders'

urlpatterns = [
    path('add/', add, name='add'),
    path('checkout/', checkout, name='checkout'),

    # ajax
    path('gestion_select_payment/', payementSelect, name="payementSelect"),
]