from django import forms
from . models import *

class UserCommentProductForm(forms.Form):
    desc = forms.CharField(widget=forms.Textarea)