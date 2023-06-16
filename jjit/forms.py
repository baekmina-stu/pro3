from django import forms
from jjit.models import Question, Answer
from ckeditor.widgets import CKEditorWidget


class QuestionForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Question
        fields = ['subject', 'content']


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }
