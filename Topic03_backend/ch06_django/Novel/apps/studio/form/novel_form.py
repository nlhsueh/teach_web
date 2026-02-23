from django import forms
from apps.novel.models import Novel


class NovelForm(forms.Form):
    title = forms.CharField(max_length=50,
                            label="title",
                            required=True,
                            error_messages={"required": "書名不得為空"})
    description = forms.CharField(max_length=500,
                                  label="description",
                                  required=True,
                                  widget=forms.TextInput,
                                  error_messages={"required": "描述不得為空"})
    state = forms.ChoiceField(label="state",
                              required=True,
                              choices=Novel.STATE_CHOICES,
                              error_messages={"required": "狀態不得為空"})
    tags = forms.CharField(max_length=50, label="tags", required=False)

    cover = forms.ImageField(label="cover", required=False)


class NewNovelForm(forms.Form):
    title = forms.CharField(max_length=50,
                            label="title",
                            required=True,
                            error_messages={"required": "書名不得為空"})
    description = forms.CharField(max_length=500,
                                  label="description",
                                  widget=forms.TextInput,
                                  required=True,
                                  error_messages={"required": "描述不得為空"})
    state = forms.ChoiceField(label="state",
                              required=True,
                              choices=Novel.STATE_CHOICES,
                              error_messages={"required": "狀態不得為空"})
    tags = forms.CharField(max_length=50, label="tags", required=False)

    cover = forms.ImageField(label="cover",
                             required=True,
                             error_messages={"required": "封面不得為空"})
