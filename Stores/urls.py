from django.urls import path
from .views import *

urlpatterns = [
    # path('forum/', views.listView, name='listView'),
    path('', StoresListView.as_view(), name='store-list'),
]