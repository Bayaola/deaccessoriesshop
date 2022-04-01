from dataclasses import field
from django import forms
from django.forms import ModelForm
from .models import MessageService


class MessageForm(ModelForm):
    class Meta:
        model = MessageService
        fields = ['service' ,'name', 'email', 'subject', 'message']
