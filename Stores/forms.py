from django import forms
from . models import *

class UserCommentProductForm(forms.Form):
    desc = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'rows': 3, 'cols': 45, "placeholder": "Write your message here."}))