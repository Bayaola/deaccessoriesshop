from django.contrib import admin
from .models import Service, MessageService
# Register your models here.

admin.site.register(Service)
admin.site.register(MessageService)