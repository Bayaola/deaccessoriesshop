from django.contrib import admin
from django.urls import path, include
from .import views

app_name = 'Services'

urlpatterns = [
    path('', views.ServicesList.as_view(), name='home'),
    path('<slug:slug>/', views.ServiceDetail.as_view(), name='service_detail'),
    path('send_message/<int:pk>', views.SendMessage.as_view(), name='send_message'),
]