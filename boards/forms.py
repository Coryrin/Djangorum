from django import forms
from .models import Post, PostComment

class PostForm(forms.ModelForm):

    title = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control"}
        ))

    body = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control"}
        ))

    class Meta:
        model = Post
        fields = ('title', 'body')

class CommentForm(forms.ModelForm):

    # Set the class and label of the comment textarea fields here.
    # Did it this way because doing it the other way ended up making the textarea look weird.
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['body'].widget.attrs.update({'class':'comment-field', 'placeholder':'Enter your comment here.'})
        self.fields['body'].label = ''

    class Meta:
        model = PostComment
        fields = ('body',)