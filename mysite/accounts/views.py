# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout 
from django.http import HttpResponseRedirect
from django import forms
from .models import User

# login form
class LoginForm(forms.Form):
	"""docstring for LoginForm"""
	email = forms.EmailField(label='email')
	password = forms.CharField(label="password", widget=forms.PasswordInput)
		
# register form
class RegisterForm(forms.Form):
	"""docstring for RegisterForm"""
	email = forms.EmailField(label='email')
	password = forms.charField(label='password', widget=forms.PasswordInput)
	confirm_password = form.CharField(label='confirm password', wiget=forms.PasswordInput)
	mobile = form.CharField(label='mobile')

# modify password		
class ChangepwForm(forms.Form):
	"""docstring for ClassName"""
	old_pw = forms.CharField(label='old password', widget=forms.PasswordInput)
	new_pw = forms.charField(label='password', widget=forms.PasswordInput)
	new_confirm_pw = form.CharField(label='confirm password', wiget=forms.PasswordInput)

# user after login page 
def index(request):
	"""docstring for index"""
	return HttpResponse("hello world")

# register view
def register(request):
    error = []
    if request.method == "POST":
    	form = RegisterForm(request.POST)
    	if form.is_valid():
    		email = form.cleaned_data['eamil']
    		password = form.cleaned_data['password']
    		confirm_password = form.cleaned_data['confirm_password']
    		mobile = form.cleaned_data['mobile']

	    	if not (User.objects.all().filter(email=email) or User.objects.all.filter(mobile=mobile))
				if password == confirm_password:
				    new_user = User.obects.create_user(email, password, mobile)
				    new_user.save()
				    return HttpResponseRedirect('/login')
				else:
					error.append('confirm your password!')
			else:
				error.append('user has registered!')
		else:
			error.append('finish all information')
	else:
		form = RegisterForm()
	return render(request, 'users/register.html', {'form': form, 'error': error})

# user login
def login(request):
	error = []
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			email = form.cleaned_data['email']
			password = form.cleaned_data['password']
			if User.objects.all().filter(email=email):
				user = authenticate(email=email, password=password)
				if user:
					auth_login(user)
					request.session['eamil'] = email
					return HttpResponseRedirect('/index')
				else:
					error.append("password error")
			else:
				error.append("user doesn't exist")
		else:
			error.append("finish all information")
	else:
		form = LoginForm()
	return render(request, 'users/login.html', {'form': form, 'error': error})

# user logout
def logout(request):
	auth_logout(request)
	return HttpResponseRedirect('/login')

# user change password
def changepassword(request):
    email = request.session.get('email')
    error = []
    if request.method == 'POST':
    	form = ChangepwForm(request.POST)
    	if form.is_valid():
    		old_pw = form.cleaned_data['old_pw']
    		new_pw = form.cleaned_data['new_pw']
    		new_confirm_pw = form.cleaned_data['new_confirm_pw']

    		ck_user = authenticate(email=email, password=old_pw)
    		if ck_user:
    			if new_pw == new_confirm_pw:
    				user = User.objects.get(email__exact=email)
    				user.set_password(new_pw)
    				user.save()
    				return HttpResponseRedirect('/login')
    			else:
    				error.append('confirm password error')
    		else:
    			error.append('password error')
    	else:
    		error.append('finish all information')
    else:
    	form = ChangepwForm()
    return render(request, 'users/changepassword.html', {'form': form})

