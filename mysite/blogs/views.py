# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django import forms

# ckeditor
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
from .models import Blog
# Create your views here.

class CreateForm(forms.Form):
	title = forms.CharField(label='title', widget=forms.widgets.TextInput(attrs={'class': 'form-control'}), required=True)
	# content = forms.CharField(label='content', widget=forms.widgets.Textarea(attrs={'class': 'form-control'}), required=True)
	content = RichTextField()


def index(request):
	"""docstring for index"""
	# blog_list = Blog.objects.all()
	return render(request, 'blogs/base.html', {})

def articles(request):
	blog_list = Blog.objects.all()
	return render(request, 'blogs/articles.html', {'blog_list': blog_list})

def article(request, id):
	print request.session.get('email')
	article_content = get_object_or_404(Blog, pk=id)
	return render(request, 'blogs/article.html', {'article': article_content})

# create blog
def create_myblog(request):
	# print request.session.email
	if request.session.get('email') is None or request.session.get('email') == '':
		return HttpResponseRedirect('/accounts/login')
	error = []
	if request.method == "POST":
		form = CreateForm(request.POST)
		if form.is_valid():
			title = form.cleaned_data['title']
			content = request.POST['editor1']
			blog = Blog.objects.create(title=title, content=content)
			blog.save()
			return HttpResponseRedirect('/blogs/articles')
		else:
			error.append('finish all informatioin')
	else:
		form = CreateForm()
	return render(request, 'blogs/create.html', {'form': form})

def delete_myblog(request, id):
	print request.session.email
	if request.session.get('email') is None or request.session.get('email') == '':
		return HttpResponseRedirect('/accounts/login')
	Blog.objects.get(id=id).delete()
	blog_list = Blog.objects.all()
	return render(request, 'blog/articles', {'blog_list': blog_list})
def update_myblog(request, id):
	if request.session.get('email') is None or request.session.get('email') == '':
		return HttpResponseRedirect('/accounts/login')
	form = get_object_or_404(Blog, pk=id)
	if request.method == "POST":
		title = request.POST['title']
		content = request.POST['editor1']
		blog = Blog.objects.get(id=id)
		blog.title = title
		blog.content = content
		blog.save()
		return HttpResponseRedirect('/blogs/articles')
	return render(request, 'blogs/update.html', {'form': form})