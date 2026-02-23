from django import forms
from django.core.exceptions import ValidationError
from ..models import User

class SignupForm(forms.Form):
    username = forms.CharField(max_length=20,
                               label="username",
                               required=True,
                               error_messages={"required": "名稱不得為空"})
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

    def clean_account(self):
        val = self.cleaned_data.get('account')

        if User.objects.filter(account=val):
            raise ValidationError("帳號已存在")
        else:
            return val

    def clean(self):
        pwd = self.cleaned_data.get("password")
        r_pwd = self.cleaned_data.get("r_password")

        if pwd != r_pwd:
            raise ValidationError("密碼不一致")
        else:
            return self.cleaned_data
