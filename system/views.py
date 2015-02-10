# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
# from system.forms import LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def index(request):
	if request.user.is_authenticated():
		return redirect('/home')
	else:
		return redirect ('/login')

def login_view(request):
	context = RequestContext(request)
	if request.method == 'POST':
		username = request.POST.get('username', False)
		password = request.POST.get('password', False)
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return redirect ('/home')
		else:
			error = u'Невалидно потребителско име или парола'
			return render_to_response('account/login.html', {'error': error}, context)

	error=''
	return render_to_response('account/login.html', {'error': error}, context)

def logout_view(request):
	logout(request)
	return redirect ('/')
	
def home(request):
	context = RequestContext(request)
	return render_to_response('menu.html', context)
