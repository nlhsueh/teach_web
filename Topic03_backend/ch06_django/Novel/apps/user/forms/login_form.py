from django import forms
from django.core.exceptions import ValidationError
from apps.user.models import User

class LoginForm(forms.Form):
    account = forms.CharField(max_length=20, 
                              label="account", 
                              error_messages={"required": "帳號不得為空"})
    password = forms.CharField(max_length=20, 
                               label="password", 
                               widget=forms.PasswordInput,
                               error_messages={"required": "密碼不得為空"})

    user_obj = None

    def clean_account(self):
        account = self.cleaned_data.get("account")
        self.user_obj = User.objects.filter(account=account).first()

        if not self.user_obj:
            raise ValidationError("帳號不存在")
        else:
            return self.cleaned_data
        
    
    def clean_password(self):        
        pwd = self.cleaned_data.get("password")

        if self.user_obj and pwd != self.user_obj.password:
            raise ValidationError("密碼錯誤")
        else:
            return self.cleaned_data

