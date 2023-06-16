from django import forms
from django.forms import ModelForm
from commentapp.models import Comment


class CommentCreationForm(ModelForm):
    parent_comment_pk = forms.IntegerField(required=False, widget=forms.HiddenInput())

    class Meta:
        model = Comment
        fields = ['content', 'parent_comment_pk']
