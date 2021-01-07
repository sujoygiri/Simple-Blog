from django import forms
from django.forms import widgets
from .models import BlogPost,Comments

class BlogPostForm(forms.ModelForm):

    class Meta():
        model = BlogPost
        fields = {'Author','Title','PostContent'}

        widgets = {
                    'Author':forms.TextInput(attrs={'class':'authorName'}),
                    'Title':forms.TextInput(attrs={'class':'textInputClass'}),
                    'PostContent':forms.Textarea(attrs={'class':'editable medium-editor-textarea postContent'})
        }

class CommentsForm(forms.ModelForm):
    
    class Meta():
        model = Comments
        fields = {'UserName','Text'}

        widgets = {
                    'Text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'}),
                    'UserName':forms.TextInput(attrs={'class':'textInputClass'})                    
        }