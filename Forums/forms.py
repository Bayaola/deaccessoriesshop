from django import forms
from .models import *

class CommentForm(forms.Form):
    desc = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'rows': 2, 'cols': 45, "placeholder": "Write your message here."}))
