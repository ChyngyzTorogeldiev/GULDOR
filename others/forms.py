from django import forms
from .models import *


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

# class ReviewForm(forms.ModelForm):
#     class Meta:
#         model = Review
#         fields = ['author', 'text']
