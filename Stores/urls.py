from django.urls import path
from .views import *

app_name = 'Stores'

urlpatterns = [
    # path('forum/', views.listView, name='listView'),
    path('', product_all, name='store_home'),
    path('<slug:slug>', product_detail, name='product_detail'),
    path('shop/<slug:category_slug>/', category_list, name='category_list'),
]