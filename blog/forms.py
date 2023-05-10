from django import forms

from blog.models import Post, Comments


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "text", "category")

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ("text", "rate")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['rate'] = forms.FloatField(max_value=5, min_value=1)