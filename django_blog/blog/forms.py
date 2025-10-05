from django import forms
from .models import Post,Comment

class PostForm(forms.Form):
    title = forms.CharField(maax_length=50,label='Title')
    check = forms.BooleanField(required = False)

class CommentForm(forms.ModelForm):
    title=forms.CharField(max_length=200,label='comment')
    check=forms.BooleanField(required=False)