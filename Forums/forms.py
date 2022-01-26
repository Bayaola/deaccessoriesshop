from django import forms
from .models import *

class CommentForm(forms.Form):
    desc = forms.CharField(widget=forms.Textarea)
