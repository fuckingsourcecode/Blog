# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django import forms

# ckeditor
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
from django.contrib.auth.decorators import login_required   

from .models import Blog, BlogType, Comment
# from accounts.models import User
from django.contrib.auth.models import User
# json
import json
from django.core.serializers.json import DjangoJSONEncoder
# Create your views here.

class CreateForm(forms.Form):
	title = forms.CharField(label='标题', widget=forms.widgets.TextInput(attrs={'class': 'form-control'}), required=True)
	bt = BlogType.objects.all()
	c= []
	for i in bt:
		c.append((i.id, i.blog_type))
	blog_type = forms.IntegerField(label='类型', widget=forms.Select(choices=c, attrs={'class': 'form-control'}))
	summary = forms.CharField(label='简介(可不填写)', widget=forms.widgets.Textarea(attrs={'class': 'form-control', 'rows': 3, 'style': 'width:98%;resize:none;'}),required=False)
	content = RichTextUploadingField()

def index(request):
	"""docstring for index"""
	blog_list = Blog.objects.all()
	
	return render(request, 'blogs/base.html', {})

def articles(request):
	blog_list = Blog.objects.all().order_by('-pub_date')
	return render(request, 'blogs/articles.html', {'blog_list': blog_list})

def article(request, id):
	article_content = get_object_or_404(Blog, pk=id)
	article_content.email = article_content.author.id
	cm = Comment.objects.filter(blog=id).order_by('-pub_date')
	return render(request, 'blogs/article.html', {'article': article_content, 'comment':cm, 'fiction': id})
def fiction(request, id):
	blogs = Blog.objects.filter(blog_type=id).order_by('-pub_date')
	return render(request, 'blogs/fiction.html', {'blogs': blogs, 'fiction': id})
def fictionorderby(request, id):
	blogs = Blog.objects.filter(blog_type=id).order_by('-hot')
	return render(request, 'blogs/fiction.html', {'blogs': blogs})
def articlesorderby(request):
	blog_list = Blog.objects.all().order_by('-hot')
	return render(request, 'blogs/articles.html', {'blog_list': blog_list})
# create blog
@login_required 
def create_myblog(request):
	# print request.session.email
	error = []
	if request.method == "POST":
		form = CreateForm(request.POST)
		print request.POST
		if form.is_valid():
			title = form.cleaned_data['title']
			content = request.POST['editor1']
			blog_type = form.cleaned_data['blog_type']
			summary = request.POST['summary']
			if summary == '':
				summary = content[:100]
			blog = Blog.objects.create(title=title, content=content, summary=summary, blog_type=BlogType.objects.get(id=blog_type),author=User.objects.get(username=request.session.get('username')))
			blog.save()
			return HttpResponseRedirect('/accounts/blog')
		else:
			error.append('finish all informatioin')
	else:
		form = CreateForm()
	return render(request, 'blogs/create.html', {'form': form})
@login_required
def delete_myblog(request, id):
	
	Blog.objects.get(id=id).delete()
	blog_list = Blog.objects.all().order_by('-pub_date')
	# return render(request, 'accounts/blog.html', {'blog_list': blog_list})
	return HttpResponseRedirect('/accounts/blog')

@login_required
def update_myblog(request, id):
	
	form = get_object_or_404(Blog, pk=id)
	if request.method == "POST":
		title = request.POST['title']
		content = request.POST['editor1']
		blog = Blog.objects.get(id=id)
		blog.title = title
		blog.content = content
		summary = request.POST['summary']
		if summary == '':
			blog.summary = content[:100]
		blog.save()
		return HttpResponseRedirect('/accounts/blog')
	return render(request, 'blogs/update.html', {'form': form})

@login_required
def good(request, id):
	blog = Blog.objects.get(id=id)
	blog.hot += 1;
	blog.save()
	return HttpResponseRedirect('/blogs/blog/'+id)
# def publish_myblog(request, id, status):
# 	if request.session.get('email') is None or request.session.get('email') == '':
# 		return HttpResponseRedirect('/accounts/login')
# 	blog = get_object_or_404(Blog, pk=id)
# 	blog.published = status
# 	blog.save()
# 	return HttpResponseRedirect('/accounts/blog')


# ***************************comment**********************************
@login_required
def create_comment(request, id):
	blog = get_object_or_404(Blog, pk=id)
	cm = Comment.objects.create(commentor=User.objects.get(username=request.session.get('username')), blog=blog, comment=request.POST['editor1'])
	return HttpResponseRedirect('/blogs/blog/'+id)
@login_required
def get_comment(request, id):
	blog = get_object_or_404(Blog, pk=id)
	cm = Comment.objects.filter(blog=blog)
	for i in cm:
		print i.comment, i.commentor
	return HttpResponseRedirect('/blogs/blog/'+id)
	return render(request, 'blogs/comment.html', {})
@login_required
def delete_comment(request, id):
	# blog = get_object_or_404(Blog, pk=id)
	cm = Comment.objects.get(id=id).delete()
	# for i in cm:
	# 	print i.comment, i.commentor
	return HttpResponseRedirect('/blogs/blog/'+id)
	return render(request, 'blogs/comment.html', {})

