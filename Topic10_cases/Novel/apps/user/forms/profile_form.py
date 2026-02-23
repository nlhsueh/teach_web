from django import forms
from django.core.exceptions import ValidationError

class ProfileForm(forms.Form):
    username = forms.CharField(max_length=20,
                               label="username",
                               required=True,
                               error_messages={"required": "使用者不得為空"})
    account = forms.CharField(max_length=20,
                              label="account",
                              required=True,
                              error_messages={"required": "帳號不得為空"})
    password = forms.CharField(max_length=20,
                               label="password",
                               required=True,
                               widget=forms.PasswordInput,
                               error_messages={"required": "密碼不得為空"})
    r_password = forms.CharField(max_length=20,
                                 label="r_password",
                                 required=True,
                                 widget=forms.PasswordInput,
                                 error_messages={"required": "確認密碼一致"})
    description = forms.CharField(max_length=255, required=False)
    avatar = forms.ImageField(required=False, label='avatar')

    def clean(self):
        pwd = self.cleaned_data.get("password")
        r_pwd = self.cleaned_data.get("r_password")

        if pwd != r_pwd:
            raise ValidationError("密碼不一致")
        else:
            return self.cleaned_data
