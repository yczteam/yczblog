from django import forms
from django_summernote.widgets import SummernoteWidget

class PostForm(forms.Form):
    
    content = forms.CharField(widget=SummernoteWidget())