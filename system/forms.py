# -*- coding: utf-8 -*-

from django import forms
from django.core.exceptions import ValidationError
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


class LoginForm(forms.ModelForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password')

	def clean(self):
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')

		user = authenticate(username=username, password=password)

	helper = FormHelper()
	helper.layout = Layout(
        Div(
	        Field('username', css_class='form-control login-field'),
	        Field('password', css_class='form-control login-field'),
	        Submit('submit', u'Вход', css_class='btn btn-primary btn-lg btn-block'),
        )
    )