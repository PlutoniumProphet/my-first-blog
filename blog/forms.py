from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    """Template django form for writing posts"""

    class Meta:
        model = Post
        fields = ('title', 'text',)


class CommentForm(forms.ModelForm):
    """Template django form for adding comments to existing posts"""

    class Meta:
        model = Comment
        fields = ('author', 'text',)
