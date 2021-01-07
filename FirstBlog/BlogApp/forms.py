from django import forms
from .models import BlogPost,Comments

class BlogPostForm(forms.ModelForm):

    class Meta():
        model = BlogPost
        field = {'Author','Title','PostContent'}