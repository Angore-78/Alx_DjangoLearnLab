from django import forms
from .models import Post

class PostForm(forms.Form):
    title = forms.CharField(maax_length=50,label='Title')
    check = forms.BooleanField(required = False)