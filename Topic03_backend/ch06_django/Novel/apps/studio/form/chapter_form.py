from django import forms
from django.core.validators import FileExtensionValidator

class ChapterForm(forms.Form):
    title = forms.CharField(max_length=50,
                            label="title",
                            required=True,
                            error_messages={"required": "書名不得為空"})
    
    content = forms.FileField(label="content",
                             required=True,
                             validators=[FileExtensionValidator(['txt'])],
                             error_messages={"required": "文章內容不得為空"})
