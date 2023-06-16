from ckeditor.widgets import CKEditorWidget
from django import forms
from articleapp.models import Article
from projectapp.models import Project

class ArticleCreationForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    project = forms.ModelChoiceField(queryset=Project.objects.all(), required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].widget.attrs['class'] = 'form-control'

    class Meta:
        model = Article
        fields = ['title', 'project', 'content', 'category']
