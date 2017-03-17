# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
import datetime
from django.http import HttpResponse
from django.utils import timezone
from .models import Blog
# Create your views here.

def index(request):
	"""docstring for index"""
	# blog_list = Blog.objects.all()
	return render(request, 'blogs/base.html', {})

def articles(request, year):
	blog_list = Blog.objects.all()
	return render(request, 'blogs/articls.html', {'blog_list': blog_list})

def article(request, blog_id):
	article_content = get_object_or_404(Blog, pk=blog_id)
	return render(request, 'blogs/blog.html', {'article': article_content})