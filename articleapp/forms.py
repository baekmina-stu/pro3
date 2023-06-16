from ckeditor.widgets import CKEditorWidget
from django import forms
from articleapp.models import Article
from projectapp.models import Project

class ArticleCreationForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    project = forms.ModelChoiceField(queryset=Project.objects.all(), required=False)

    class Meta:
        model = Article
        fields = ['title', 'project', 'content']
