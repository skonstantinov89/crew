# -*- coding: utf-8 -*-
from django import forms
from django.core.exceptions import ValidationError
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from persons.models import Persons
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


class newPerson(forms.ModelForm):
    name = forms.CharField()
    sirname = forms.CharField()
    familyname = forms.CharField()

	def __init__(self, arg):
		super(newPerson, self).__init__()
		self.arg = arg
		print (self.arg)
    		
    class Meta:
        model = Persons
        fields = ('username', 'password')

	def clean(self):
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')

		user = authenticate(username=username, password=password)

	helper = FormHelper()
	helper.layout = Layout(
	        Field('name', css_class='form-control'),
	        Field('sirname', css_class='form-control'),
	        Field('familyname', css_class='form-control'),

	        Submit('submit', 'Submit', css_class='btn btn-primary btn-lg btn-block'),
    )
    		