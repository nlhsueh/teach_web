from django import forms

class VolumnForm(forms.Form):
    title = forms.CharField(max_length=50,
                            label="title",
                            required=True,
                            error_messages={"required": "書名不得為空"})
