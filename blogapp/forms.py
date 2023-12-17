from django import forms
from .models import Write
from .models import Comment

class WriteForm(forms.ModelForm):
  class Meta: 
    model = Write 
    fields = '__all__'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']