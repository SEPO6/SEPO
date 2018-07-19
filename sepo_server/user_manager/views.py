# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template import Context
from django.template.loader import get_template

from django.shortcuts import render
from django.http.response import HttpResponse
from django.template.context_processors import csrf
from user_manager.forms import LoginForm, JoinForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_auth
from django.shortcuts import redirect
from django.contrib.auth.models import User
from ranking.models import Score
from ranking.views import update_ranking

# Create your views here.

def login(req):
	template = get_template('LoginPage.html')

	context = {'login_form' : LoginForm()}

	return render(req,'LoginPage.html',context)

def login_validate(req):
	
	login_form_data = LoginForm(req.POST)

	if login_form_data.is_valid():
		un = login_form_data.cleaned_data['username']
		pw = login_form_data.cleaned_data['password']
		usero = authenticate(username = un, password = pw)
		if usero is not None:
			if usero.is_active:
				login_auth(req,usero)
				return redirect('/')

			
		else:
			return HttpResponse('No User or Password Error!')
	else:
		return HttpResponse('Abnormal Login Form!')

	return HttpResponse('Unknown Error!')

def join(req):
	
	if req.method == 'POST':
		form_data = JoinForm(req.POST)
		if form_data.is_valid():
			usern = form_data.cleaned_data['username']
			passw = form_data.cleaned_data['password']
			pwcheck = form_data.cleaned_data['password_check']

			if passw == pwcheck:
				if not User.objects.filter(username = usern).exists():
					User.objects.create_user(usern, '', passw)
					Score.objects.create(username=usern)
					update_ranking()
					return redirect('/user/login/')
				else:
					return HttpResponse('That ID Already Exists!')
			else:
				return HttpResponse('Check Password')

	else:
		form_data = JoinForm()
				
	context = {'join_form' : form_data}	
			

	return render(req,'SignUp.html',context)


