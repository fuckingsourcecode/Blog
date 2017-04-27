# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout 
from django.http import HttpResponseRedirect
from django import forms
from .models import User
from django.contrib.auth.hashers import make_password, check_password
from blogs.models import Blog

# login form
class LoginForm(forms.Form):
	"""docstring for LoginForm"""
	email = forms.EmailField(label='email', widget=forms.widgets.EmailInput(attrs={'class': 'form-contorl'}))
	password = forms.CharField(label="password", widget=forms.widgets.PasswordInput(attrs={'class': 'form-contorl'}))
		
# register form
class RegisterForm(forms.Form):
	"""docstring for RegisterForm"""
	email = forms.EmailField(label='email')
	password = forms.CharField(label='password', widget=forms.widgets.PasswordInput(attrs={'class': 'form-contorl'}))
	confirm_password = forms.CharField(label='confirm password', widget=forms.widgets.PasswordInput(attrs={'class': 'form-contorl'}))
	mobile = forms.CharField(label='mobile', widget=forms.widgets.TextInput(attrs={'class': 'form-contorl'}))

# modify password		
class ChangepwForm(forms.Form):
	"""docstring for ClassName"""
	old_pw = forms.CharField(label='old password', widget=forms.widgets.PasswordInput(attrs={'class': 'form-contorl'}))
	new_pw = forms.CharField(label='password', widget=forms.widgets.PasswordInput(attrs={'class': 'form-contorl'}))
	new_confirm_pw = forms.CharField(label='confirm password', widget=forms.widgets.PasswordInput(attrs={'class': 'form-contorl'}))

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
			email = form.cleaned_data['email']
			password = form.cleaned_data['password']
			confirm_password = form.cleaned_data['confirm_password']
			mobile = form.cleaned_data['mobile']
			if not User.objects.all().filter(email=email):
				if password == confirm_password:
					password = password
					new_user = User.objects.create(email=email, password=password, mobile=mobile)
					new_user.save()
					return HttpResponseRedirect('/accounts/login')
				else:
					error.append('confirm password')
			else:
				error.append('email has registered')
		else:
			error.append('finish all')
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
			if User.objects.all().get(email=email):
				user = User.objects.get(email__exact = email,password__exact = password)
				if user is not None:
					auth_login(request, user)
					request.session['email'] = email
					print request.session['email']
					# authenticate(email=email, password=password)
					return HttpResponseRedirect('/blogs/article/2')
				else:
					error.append("password error")
			else:
				return HttpResponseRedirect('/accounts/register')
		else:
			error.append("finish all information")
	else:
		form = LoginForm()
	print error
	return render(request, 'users/login.html', {'form': form, 'error': error})

# user logout
def logout(request):
	auth_logout(request)
	return HttpResponseRedirect('/accounts/login')

# user change password
def changepassword(request):
    email = request.session.get('email')
    if email is None or email == '':
    	return HttpResponseRedirect('/accounts/login')
    error = []
    if request.method == 'POST':
    	form = ChangepwForm(request.POST)
    	if form.is_valid():
    		old_pw = form.cleaned_data['old_pw']
    		new_pw = form.cleaned_data['new_pw']
    		new_confirm_pw = form.cleaned_data['new_confirm_pw']

    		ck_user = User.objects.get(email__exact=email, password=old_pw)
    		if ck_user:
    			if new_pw == new_confirm_pw:
    				user = User.objects.get(email__exact=email)
    				user.password = new_pw
    				user.save()
    				auth_logout(request)
    				print request.session.get('email')
    				return HttpResponseRedirect('/accounts/login')
    			else:
    				error.append('confirm password error')
    		else:
    			error.append('password error')
    	else:
    		error.append('finish all information')
    else:
    	form = ChangepwForm()
    return render(request, 'users/changepassword.html', {'form': form})

# let user get their own blogs
def blog(request):
	if request.session.get('email') is None or request.session.get('email') == '':
		return HttpResponseRedirect('/accounts/login')
	blogs = Blog.objects.all()
	# blogs.num = 0
	for i in range(0, len(blogs)):
		blogs[i].num = i
	return render(request, 'users/blog.html', {'blogs': blogs})

    

