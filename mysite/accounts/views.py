# -*- coding: utf-8 -*-
import sys
from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout 
from django.http import HttpResponseRedirect, JsonResponse
from django import forms
# from .models import User
from django.contrib.auth.hashers import make_password, check_password
from blogs.models import Blog, BlogType, Comment
import json
from django.core.serializers.json import DjangoJSONEncoder
# code 
from captcha.fields import CaptchaField
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required 
import datetime
reload(sys)
sys.setdefaultencoding('utf-8')
# login form
class LoginForm(forms.Form):
	"""docstring for LoginForm"""
	username = forms.CharField(label='用户名', widget=forms.widgets.TextInput(attrs={'class': 'form-control'}), required=True)
	password = forms.CharField(label="密码", widget=forms.widgets.PasswordInput(attrs={'class': 'form-control'}), required=True)
	captcha = CaptchaField(error_messages={"invalid": u"验证码错误"})
		
# register form
class RegisterForm(forms.Form):
	"""docstring for RegisterForm"""
	username = forms.CharField(label='用户名', widget=forms.widgets.TextInput(attrs={'class': 'form-control'}), required=True)
	email = forms.EmailField(label='邮箱', widget=forms.widgets.EmailInput(attrs={'class': 'form-control'}), required=True)
	password = forms.CharField(label='密码', widget=forms.widgets.PasswordInput(attrs={'class': 'form-control'}), required=True)
	confirm_password = forms.CharField(label='确认密码', widget=forms.widgets.PasswordInput(attrs={'class': 'form-control'}), required=True)
	# mobile = forms.CharField(label='手机', widget=forms.widgets.TextInput(attrs={'class': 'form-control'}))
	captcha = CaptchaField(error_messages={"invalid": u"验证码错误"})

# modify password		
class ChangepwForm(forms.Form):
	"""docstring for ClassName"""
	old_pw = forms.CharField(label='原始密码', widget=forms.widgets.PasswordInput(attrs={'class': 'form-control'}), required=True)
	new_pw = forms.CharField(label='密码', widget=forms.widgets.PasswordInput(attrs={'class': 'form-control'}), required=True)
	new_confirm_pw = forms.CharField(label='确认密码', widget=forms.widgets.PasswordInput(attrs={'class': 'form-control'}), required=True)
# self information
class InformationForm(forms.Form):
	email = forms.EmailField(label='邮箱', widget=forms.widgets.EmailInput(attrs={'class': 'form-control'}), required=True)
	# mobile = forms.CharField(label='手机', widget=forms.widgets.TextInput(attrs={'class': 'form-control'}))
	# occupation = forms.CharField(label='职业', widget=forms.widgets.TextInput(attrs={'class': 'form-control'}))
	# address = forms.CharField(label='地址', widget=forms.widgets.TextInput(attrs={'class': 'form-control'})) 
	# url = forms.URLField(label='个人网站', widget=forms.widgets.URLInput(attrs={'class': 'form-control'}))
# user after login page 
def index(request):
	"""docstring for index"""
	return HttpResponse("hello world")

# register view
def register(request):
	reload(sys)
	sys.setdefaultencoding('utf-8')
	error = []
	if request.method == "POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			email = form.cleaned_data['email']
			password = form.cleaned_data['password']
			confirm_password = form.cleaned_data['confirm_password']
			# mobile = form.cleaned_data['mobile']
			if not User.objects.all().filter(email=email):
				if not User.objects.all().filter(username=username):
					if password == confirm_password:
						password = password
						new_user = User.objects.create_user(username=username, email=email, password=password, is_staff=True, is_active=True)
						new_user.save()
						return HttpResponseRedirect('/accounts/login')
					else:
						error.append("两次密码不一致")
				else:
						error.append("该手机已注册")
			else:
				error.append("该邮箱已注册")
	else:
		form = RegisterForm()
	return render(request, 'users/register.html', {'form': form, 'error': error})
class DateEncoder(json.JSONEncoder):  
    def default(self, obj):  
        if isinstance(obj, datetime.datetime):  
            return obj.strftime('%Y-%m-%d %H:%M:%S')  
        elif isinstance(obj, date):  
            return obj.strftime("%Y-%m-%d")  
        else:  
            return json.JSONEncoder.default(self, obj) 
# user login
def login(request):
	nextto = request.GET.get('next') or '/accounts/blog'
	error = []
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			print username, password
			if User.objects.filter(username=username).exists():
				user = authenticate(username=username,password=password)
				print user
				if user is not None:
					user = User.objects.get(username=username)
					request.session['last_login'] = json.dumps(user.last_login, cls=DateEncoder)
					print request.session['last_login']
					auth_login(request, user)
					request.session['username'] = username
					# authenticate(email=email, password=password)
					return HttpResponseRedirect(nextto)
				else:
						error.append("密码错误")					
			else:
				error.append("用户不存在")
	else:
		form = LoginForm()
	print error
	return render(request, 'users/login.html', {'form': form, 'error': error})

# user logout
def logout(request):
	auth_logout(request)
	request.session.flush()
	return HttpResponseRedirect('/accounts/login')

# user change password
@login_required 
def changepassword(request):
    error = []
    if request.method == 'POST':
    	form = ChangepwForm(request.POST)
    	if form.is_valid():
    		old_pw = form.cleaned_data['old_pw']
    		new_pw = form.cleaned_data['new_pw']
    		new_confirm_pw = form.cleaned_data['new_confirm_pw']

    		ck_user = authenticate(username=request.session.get('username'), password=old_pw)
    		print ck_user
    		if ck_user is not None:
    			if new_pw == new_confirm_pw:
    				u = User.objects.get(username=request.session.get('username'))
    				u.set_password(new_pw)
    				u.save()
    				auth_logout(request)
  
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
@login_required 
def blog(request):
	author=User.objects.get(username=request.session.get('username'))
	blogs = Blog.objects.filter(author=author).order_by('-pub_date')
	fiction = BlogType.objects.all()
	for i in range(0, len(blogs)):
		blogs[i].num = i
		print request.session.get('username')
		blogs[i].count = (Comment.objects.filter(blog=blogs[i], pub_date__gte=json.loads(request.session.get('last_login')))).count()
		print author.last_login
		# blog[i].count = 1
	return render(request, 'users/blog.html', {'blogs': blogs, 'fiction': fiction})
@login_required 
def information(request):	
	if request.method == 'POST':
		form = InformationForm(request.POST)
		if form.is_valid():
			email = form.cleaned_data['email']
			# mobile = form.cleaned_data['mobile']
			# url = form.cleaned_data['url']
			# address = form.cleaned_data['address']
			# occupation = form.cleaned_data['occupation']
			user = User.objects.get(email__exact=request.session.get('email'))
			if user:
				user.email = email
				# user.mobile = mobile
				# user.url = url
				# user.address = address
				# user.occupation = occupation
				user.save()
				request.session.username = user.username
				return HttpResponseRedirect('/accounts/blog')
	else:
		username = request.session.get('username')
		user = User.objects.get(username = username)
		# form = InformationForm(initial={'email': user.email, 'address': user.address, 'occupation': user.occupation, 'url': user.url, 'mobile': user.mobile
		form = InformationForm(initial={'email': user.email})
	return render(request, 'users/information.html', {'form': form})

def query(request):
	return render(request, 'users/query.html', {})

def queryemail(request):
	if request.method == 'GET':
		email = request.GET['email']
		user = User.objects.get(email=email)
		blogs = Blog.objects.filter(author=user).order_by('-pub_date').values('id', 'title', 'blog_type', 'hot', 'pub_date')
		for i in blogs:
			print i['blog_type']
			i['blog_type'] = BlogType.objects.get(id=i['blog_type']).blog_type
		return HttpResponse(json.dumps(list(blogs), cls=DjangoJSONEncoder))
@login_required 
def account(request, id):
	print id
	user = User.objects.get(id=id)
	blogs = Blog.objects.filter(author=user).order_by('-pub_date')
	return render(request, 'users/user.html', {'blogs': blogs})
@login_required
def getfictionblog(request):
	if request.method == 'GET':
		id = request.GET['id']
		print id
		user = User.objects.get(username=request.session.get('username'))
		blogs = Blog.objects.filter(author=user, blog_type=id).order_by('-pub_date').values('id', 'title', 'blog_type', 'hot', 'pub_date')
		for i in blogs:
			print i['blog_type']
			i['blog_type'] = BlogType.objects.get(id=i['blog_type']).blog_type
		return HttpResponse(json.dumps(list(blogs), cls=DjangoJSONEncoder))
  




    

