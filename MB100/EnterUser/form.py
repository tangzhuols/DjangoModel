# coding:utf-8
__author__ = 'mingwang'
from django import forms
from voModel.models import CoComUser
from bootstrap_toolkit.widgets import BootstrapDateInput, BootstrapTextInput, BootstrapUneditableInput


class LoginForm(forms.Form):
    userName = forms.CharField(
        required=True,
        label=u"用户名",
        error_messages={'required': u'请输入用户名'},
        widget=forms.TextInput(
            attrs={'placeholder': u'用户名'}
        ),
    )
    userPwd = forms.CharField(
        required=True,
        label=u'密码',
        error_messages={'required': u'请输入密码'},
        widget=forms.PasswordInput(
            attrs={'placeholder': u'密码'}
        ),
    )
    def clean(self):
        if not self.is_valid():
            raise forms.ValidationError(u'用户和密码必须填写')
        else:
            cleaned_data = super(LoginForm, self).clean()
